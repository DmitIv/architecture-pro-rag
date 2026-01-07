#! /usr/bin/env python3

import pprint
import sys
import time
from pathlib import Path
from typing import Iterator, NamedTuple

import chromadb
import torch
import torch.nn.functional as F
import tqdm
from chromadb import Documents, EmbeddingFunction, Embeddings
from transformers import AutoModel, AutoTokenizer


class EmbeddingsModel(EmbeddingFunction):
    _MODEL = "sentence-transformers/all-MiniLM-L6-v2"

    def __init__(self) -> None:
        self._model = AutoModel.from_pretrained(self._MODEL)
        self._tokenizer = AutoTokenizer.from_pretrained(self._MODEL)

    @staticmethod
    def _mean_pooling(model_output, attention_mask):
        token_embeddings = model_output[0]
        input_mask_expanded = (
            attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        )
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(
            input_mask_expanded.sum(1), min=1e-9
        )

    def __call__(self, sentences: Documents) -> Embeddings:
        encoded_input = self._tokenizer(
            sentences, padding=True, truncation=True, return_tensors="pt"
        )
        with torch.no_grad():
            model_output = self._model(**encoded_input)
        sentence_embeddings = self._mean_pooling(
            model_output, encoded_input["attention_mask"]
        )
        computed = F.normalize(sentence_embeddings, p=2, dim=1).detach().cpu().numpy()
        return [c for c in computed]


class Fact(NamedTuple):
    data: str
    path: str
    name: str


class FactsStorage:
    _TARGET_SUFFIX = ".md"

    __slots__ = ["_facts_paths"]

    def __init__(self, base_dir: Path) -> None:
        base_dir = base_dir.resolve()
        self._facts_paths: tuple[Path, ...] = tuple(
            path.resolve()
            for path in base_dir.iterdir()
            if path.is_file() and path.suffix == self._TARGET_SUFFIX
        )

    def __len__(self) -> int:
        return len(self._facts_paths)

    def __iter__(self) -> Iterator[Fact]:
        for fact_path in tqdm.tqdm(self._facts_paths, desc="Loading facts: "):
            with open(fact_path, "r") as fact_file:
                fact_data = fact_file.read()
            yield Fact(data=fact_data, path=str(fact_path), name=fact_path.name)


class Index:
    _DEFAULT_QUERY_RESPONSES = 1
    _METADATA_SOURCE = "source"

    def __init__(self, path: Path) -> None:
        self._client = chromadb.PersistentClient(path.resolve())
        self._collection = self._client.create_collection(
            name="facts",
            get_or_create=True,
            embedding_function=EmbeddingsModel(),
        )

    def __len__(self) -> int:
        return self._collection.count()

    def add(self, storage: FactsStorage) -> None:
        ids: list[str] = []
        documents: list[str] = []
        metadata: list[dict[str, str]] = []
        for fact in storage:
            ids.append(fact.name)
            documents.append(fact.data)
            metadata.append({self._METADATA_SOURCE: fact.path})

        self._collection.add(
            ids=ids,
            metadatas=metadata,  # type: ignore
            documents=documents,
        )

    def query(self, text: str, n: int | None = None) -> tuple[Fact, ...]:
        if n is None:
            n = self._DEFAULT_QUERY_RESPONSES

        print(f"Input query: {text}")
        result = self._collection.query(query_texts=text, n_results=n)
        if result["documents"] is None:
            raise RuntimeError("failed to extract documents")
        if result["metadatas"] is None:
            raise RuntimeError("failed to extract metadata")
        return tuple(
            Fact(
                data=result["documents"][0][i],
                name=result["ids"][0][i],
                path=str(result["metadatas"][0][i][self._METADATA_SOURCE]),
            )
            for i in range(len(result["ids"][0]))
        )


def compute_index(facts: FactsStorage, index_path: str) -> Index:
    index = Index(Path(index_path))
    start_time = time.perf_counter()
    index.add(facts)
    elapsed_time = time.perf_counter() - start_time
    print(f"Computing index elapsed: {elapsed_time:.4f} seconds")
    print(f"Collection size: {len(index)}")
    return index


def main() -> None:
    facts_base_dir = sys.argv[1]
    facts = FactsStorage(Path(facts_base_dir))
    index = compute_index(facts, "./facts-rag")
    response = index.query("What is The Silent Administrators or the Enumerators?", 4)
    pprint.pprint(
        tuple({"Text": r.data, "ID": r.name} for r in response),
        width=120,
        indent=4,
    )


if __name__ == "__main__":
    main()

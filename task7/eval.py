#! /usr/bin/env python3
import string

import pandas as pd
import torch
import torch.nn.functional as F
from sentence_transformers import util
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


def main():
    with open("golden_questions.txt", "r") as golden_test_file:
        data = golden_test_file.readlines()

    qs = {}
    for i in range(0, len(data), 2):
        qs[data[i].lower().strip()] = data[i + 1]

    correct = 0
    embeddings = EmbeddingsModel()
    for _, row in pd.read_csv("logs.csv").iterrows():
        q = row["query"].lower().strip().strip("'")
        if q not in qs:
            continue
        expected = (
            qs[q].translate(str.maketrans("", "", string.punctuation)).replace("\n", "")
        ).lower().strip().strip("'")
        received = row["result"].lower().strip().strip("'")
        embs = embeddings([expected, received])
        sim = util.cos_sim(embs[0], embs[1]).detach().cpu().numpy()[0, 0]
        print(q, expected, received, sim)
        if sim > 0.7:
            correct += 1

    print(f"Accuracy: {correct / len(qs) * 100:.4f}%")


if __name__ == "__main__":
    main()

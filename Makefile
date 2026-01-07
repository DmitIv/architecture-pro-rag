.PHONY: install
install:
	poetry install --no-root --no-interaction --no-ansi

.PHONY: compute-embeddings
compute-index:
	poetry run task3/index.py task2/facts
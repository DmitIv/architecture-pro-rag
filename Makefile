-include .env
export

.PHONY: install
install:
	poetry install --no-root --no-interaction --no-ansi

.PHONY: compute-embeddings
compute-index: install
	poetry run task3/index.py task2/facts

.PHONY: run-bot
run-bot: install
	facts_base_dir=task2/facts index_path=facts-rag poetry run task4/bot.py

.PHONY: evaluate-accuracy
evaluate-accuracy: install
	poetry run task7/eval.py
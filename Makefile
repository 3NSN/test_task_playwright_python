.PHONY: setup test lint clean

setup:
	pip install uv
	uv venv
	uv pip install tox tox-uv

test:
	uv run tox -- --headed

lint:
	uv run tox -e lint

clean:
	rm -rf .tox
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf dist
	find . -type d -name "__pycache__" -exec rm -rf {} +
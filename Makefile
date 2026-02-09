.PHONY: setup test lint clean

setup:
	uv sync --dev
	uv run pre-commit install

test:
	uv run tox

test-ui:
	uv run tox -- --headed

lint:
	uv run tox -e lint

clean:
	rm -rf .tox
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf dist
	find . -type d -name "__pycache__" -exec rm -rf {} +
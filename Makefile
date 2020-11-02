install:
	@poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest tests -vv

.PHONY: install lint
install:
	@poetry install

lint:
	poetry run flake8 gendiff

.PHONY: install lint
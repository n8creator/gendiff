install:
	@poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -v --verbose --cov=gendiff tests/

coverage_xml:
	poetry run coverage xml

run_json:
	poetry run gendiff tests/fixtures/input.json  tests/fixtures/output.json

run_yml:
	poetry run gendiff tests/fixtures/input.yml  tests/fixtures/output.yml

.PHONY: install lint test coverage_xml run_json run_yml
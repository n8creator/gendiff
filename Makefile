install:
	@poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -v --verbose -s --cov=gendiff tests/

coverage_xml:
	poetry run coverage xml

run_json:
	poetry run gendiff tests/fixtures/1_input.json  tests/fixtures/1_output.json -f plain

run_yml:
	poetry run gendiff tests/fixtures/2_input.yml  tests/fixtures/2_output.yml

run_json_nest:
	poetry run gendiff tests/fixtures/3_nested_input.json  tests/fixtures/3_nested_output.json

run_yml_nest:
	poetry run gendiff tests/fixtures/4_nested_input.yml  tests/fixtures/4_nested_output.yml

.PHONY: install lint test coverage_xml run_json run_yml run_json_nest run_yml_nest
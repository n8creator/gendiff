install:
	@poetry install

lint:
	poetry run flake8 gendiff

test: lint
	poetry run pytest -v --verbose -s --cov=gendiff tests/

coverage_xml:
	poetry run coverage xml

run_json:
	poetry run gendiff tests/fixtures/arg_files/file1.json  tests/fixtures/arg_files/file2.json

run_yml:
	poetry run gendiff tests/fixtures/arg_files/file1.yml  tests/fixtures/arg_files/file2.yml

run_json_nest:
	poetry run gendiff tests/fixtures/arg_files/nested1.json  tests/fixtures/arg_files/nested2.json

run_json_nest_plain:
	poetry run gendiff tests/fixtures/arg_files/nested1.json  tests/fixtures/arg_files/nested2.json --format plain

run_json_nest_json:
	poetry run gendiff tests/fixtures/arg_files/nested1.json  tests/fixtures/arg_files/nested2.json --format json

run_yml_nest:
	poetry run gendiff tests/fixtures/arg_files/nested1.yml  tests/fixtures/arg_files/nested2.yml

run_yml_nest_plain:
	poetry run gendiff tests/fixtures/arg_files/nested1.yml  tests/fixtures/arg_files/nested2.yml -f plain

run_yml_nest_json:
	poetry run gendiff tests/fixtures/arg_files/nested1.yml  tests/fixtures/arg_files/nested2.yml -f json

.PHONY: install lint test coverage_xml run_json run_yml run_json_nest run_yml_nest
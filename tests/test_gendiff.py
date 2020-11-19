from gendiff.generate_diff import generate_difference
from gendiff.format_diff import formatted_diff
import pytest


@pytest.mark.parametrize('input_file, output_file, expected', [
                (
                    # Params for testing flat JSON files
                    'tests/fixtures/arg_files/file1.json',
                    'tests/fixtures/arg_files/file2.json',
                    'tests/fixtures/expected_outputs/default_for_flat.txt'
                ),
                (
                    # Params for testing flat YML files
                    'tests/fixtures/arg_files/file1.yml',
                    'tests/fixtures/arg_files/file2.yml',
                    'tests/fixtures/expected_outputs/default_for_flat.txt'
                ),
                (
                    # Params for testing nested JSON files
                    'tests/fixtures/arg_files/nested_file1.json',
                    'tests/fixtures/arg_files/nested_file2.json',
                    'tests/fixtures/expected_outputs/default_for_nested.txt'
                ),
                (
                    # Params for testing nested YML files
                    'tests/fixtures/arg_files/nested_file1.yml',
                    'tests/fixtures/arg_files/nested_file2.yml',
                    'tests/fixtures/expected_outputs/default_for_nested.txt'
                ),
            ])
def test_default_output(input_file, output_file, expected):
    """Test for json & yml files with Default output."""

    check = open(expected, 'r', encoding='UTF-8')
    assert formatted_diff(input_file, output_file) == check.read()
    check.close()


@pytest.mark.parametrize('input_file, output_file, expected', [
                (
                    # Params for testing nested JSON files with Plain output
                    'tests/fixtures/arg_files/nested_file1.json',
                    'tests/fixtures/arg_files/nested_file2.json',
                    'tests/fixtures/expected_outputs/plain_for_nested.txt'
                ),
                (
                    # Params for testing nested YML files with Plain output
                    'tests/fixtures/arg_files/nested_file1.yml',
                    'tests/fixtures/arg_files/nested_file2.yml',
                    'tests/fixtures/expected_outputs/plain_for_nested.txt'
                )
            ])
def test_plain_output(input_file, output_file, expected):
    """Test for json & yml files with Plain output."""

    check = open(expected, 'r', encoding='UTF-8')
    assert formatted_diff(input_file, output_file, 'plain') == check.read()
    check.close()


@pytest.mark.parametrize('input_file, output_file, expected', [
                (
                    # Params for testing nested JSON files with JSON output
                    'tests/fixtures/arg_files/nested_file1.json',
                    'tests/fixtures/arg_files/nested_file2.json',
                    'tests/fixtures/expected_outputs/json_for_nested.txt'
                ),
                (
                    # Params for testing nested YML files with JSON output
                    'tests/fixtures/arg_files/nested_file1.yml',
                    'tests/fixtures/arg_files/nested_file2.yml',
                    'tests/fixtures/expected_outputs/json_for_nested.txt'
                )
            ])
def test_json_output(input_file, output_file, expected):
    """Test for json & yml files with JSON output."""

    check = open(expected, 'r', encoding='UTF-8')
    assert formatted_diff(input_file, output_file, 'json') == check.read()
    check.close()

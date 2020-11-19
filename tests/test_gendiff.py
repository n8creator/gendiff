from gendiff.format_diff import formatted_diff
import pytest


@pytest.mark.parametrize('input_file, output_file, expected_output, format', [
        ('file1.json', 'file2.json', 'default_for_flat.txt', None),
        ('file1.yml', 'file2.yml', 'default_for_flat.txt', None),
        ('nested1.json', 'nested2.json', 'default_for_nested.txt', None),
        ('nested1.yml', 'nested2.yml', 'default_for_nested.txt', None),
        ('nested1.json', 'nested2.json', 'plain_for_nested.txt', 'plain'),
        ('nested1.yml', 'nested2.yml', 'plain_for_nested.txt', 'plain'),
        ('nested1.json', 'nested2.json', 'json_for_nested.txt', 'json'),
        ('nested1.yml', 'nested2.yml', 'json_for_nested.txt', 'json'),
    ])
def test_default_output(input_file, output_file, expected_output, format):

    # Argument & Expected Output files paths
    args_path = 'tests/fixtures/arg_files/'
    outputs_path = 'tests/fixtures/expected_outputs/'

    # Generating full path to Argument's and Expected Output files
    input = f"{args_path}{input_file}"
    output = f"{args_path}{output_file}"
    expected_output = f"{outputs_path}{expected_output}"

    # PyTest execution
    check = open(expected_output, 'r', encoding='UTF-8')
    assert formatted_diff(input, output, format) == check.read()
    check.close()

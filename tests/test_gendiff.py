from gendiff import generate_diff
import pytest
import json
import os


@pytest.mark.parametrize('file1, file2, output, format', [
    ('file1.json', 'file2.json', 'default_for_flat.txt', None),
    ('file1.yml', 'file2.yml', 'default_for_flat.txt', None),
    ('nested1.json', 'nested2.json', 'default_for_nested.txt', None),
    ('nested1.yml', 'nested2.yml', 'default_for_nested.txt', None),
    ('nested1.json', 'nested2.json', 'plain_for_nested.txt', 'plain'),
    ('nested1.yml', 'nested2.yml', 'plain_for_nested.txt', 'plain'),
    ('nested1.json', 'nested2.json', 'json_for_nested.txt', 'json'),
    ('nested1.yml', 'nested2.yml', 'json_for_nested.txt', 'json'),
    ])  # noqa: E123
def test_default_output(file1, file2, output, format):

    # Argument & Expected Output files paths
    args_path = 'tests/fixtures/arg_files/'
    outputs_path = 'tests/fixtures/expected_outputs/'

    # Generating full path to Argument's and Expected Output files
    file1 = os.path.join(args_path, file1)
    file2 = os.path.join(args_path, file2)
    output = os.path.join(outputs_path, output)

    # Generating diff
    diff = generate_diff(file1, file2, format)

    # PyTest execution
    with open(output, 'r', encoding='UTF-8') as expected:
        if format == 'json':
            assert json.loads(diff) == json.load(expected)
        else:
            assert diff == expected.read()

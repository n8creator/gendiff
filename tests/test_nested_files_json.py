from gendiff.generate_diff import generate_diff
from gendiff.to_json_converter import file_to_json
from gendiff.format_diff import format_diff


def test_nested_diff_json_plain():
    """Test for nested JSON files with plain output."""
    check = open('tests/fixtures/3_nested_diff_json_json.txt',
                 'r', encoding='UTF-8')
    diff = generate_diff(file_to_json('tests/fixtures/3_nested_input.json'),
                         file_to_json('tests/fixtures/3_nested_output.json'))
    assert format_diff(diff, 'json') == check.read()
    check.close()


def test_nested_diff_yml_plain():
    """Test for nested YML/YAML files with plain output."""
    check = open('tests/fixtures/4_nested_diff_yml_json.txt',
                 'r', encoding='UTF-8')
    diff = generate_diff(file_to_json('tests/fixtures/4_nested_input.yml'),
                         file_to_json('tests/fixtures/4_nested_output.yml'))
    assert format_diff(diff, 'json') == check.read()
    check.close()

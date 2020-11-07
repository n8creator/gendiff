from gendiff.generate_diff import generate_diff
from gendiff.to_json_converter import file_to_json
from gendiff.format_diff import format_diff


def test_diff_json():
    """Test for flat JSON files."""
    check = open('tests/fixtures/1_diff_json.txt', 'r', encoding='UTF-8')
    diff = generate_diff(file_to_json('tests/fixtures/1_input.json'),
                         file_to_json('tests/fixtures/1_output.json'))
    assert format_diff(diff) == check.read()
    check.close()


def test_diff_yml():
    """Test for flat YML/YAML files."""
    check = open('tests/fixtures/2_diff_yml.txt', 'r', encoding='UTF-8')
    diff = generate_diff(file_to_json('tests/fixtures/2_input.yml'),
                         file_to_json('tests/fixtures/2_output.yml'))
    assert format_diff(diff) == check.read()
    check.close()

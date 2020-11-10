from gendiff.generate_diff import generate_diff
from gendiff.to_json_converter import file_to_json as to_json
from gendiff.format_diff import format_diff


def test_flat():
    """Tests for flat files with Standard output."""

    # Test for flat JSON files
    check = open('tests/fixtures/outputs/json_flat_standard.txt',
                 'r', encoding='UTF-8')
    diff = generate_diff(to_json('tests/fixtures/inputs/input.json'),
                         to_json('tests/fixtures/inputs/output.json'))
    assert format_diff(diff) == check.read()
    check.close()

    # Test for flat YML files
    check = open('tests/fixtures/outputs/yml_flat_standard.txt',
                 'r', encoding='UTF-8')
    diff = generate_diff(to_json('tests/fixtures/inputs/input.yml'),
                         to_json('tests/fixtures/inputs/output.yml'))
    assert format_diff(diff) == check.read()
    check.close()


def test_nest():
    """Tests for nested files with Standard output."""

    # Test for nested JSON files
    check = open('tests/fixtures/outputs/json_nest_standard.txt',
                 'r', encoding='UTF-8')
    diff = generate_diff(to_json('tests/fixtures/inputs/nest_input.json'),
                         to_json('tests/fixtures/inputs/nest_output.json'))
    assert format_diff(diff) == check.read()
    check.close()

    # Test for nested YML files
    check = open('tests/fixtures/outputs/yml_nest_standard.txt',
                 'r', encoding='UTF-8')
    diff = generate_diff(to_json('tests/fixtures/inputs/nest_input.yml'),
                         to_json('tests/fixtures/inputs/nest_output.yml'))
    assert format_diff(diff) == check.read()
    check.close()


def test_nested_formatted():
    """Tests for nested files with Plain or JSON output."""

    # Test for nested JSON files with Plain output
    check = open('tests/fixtures/outputs/json_nest_plain.txt',
                 'r', encoding='UTF-8')
    diff = generate_diff(to_json('tests/fixtures/inputs/nest_input.json'),
                         to_json('tests/fixtures/inputs/nest_output.json'))
    assert format_diff(diff, 'plain') == check.read()
    check.close()

    # Test for nested JSON files with JSON output
    check = open('tests/fixtures/outputs/json_nest_json.txt',
                 'r', encoding='UTF-8')
    diff = generate_diff(to_json('tests/fixtures/inputs/nest_input.json'),
                         to_json('tests/fixtures/inputs/nest_output.json'))
    assert format_diff(diff, 'json') == check.read()
    check.close()

    # Test for nested YML files with Plain output
    check = open('tests/fixtures/outputs/yml_nest_plain.txt',
                 'r', encoding='UTF-8')
    diff = generate_diff(to_json('tests/fixtures/inputs/nest_input.yml'),
                         to_json('tests/fixtures/inputs/nest_output.yml'))
    assert format_diff(diff, 'plain') == check.read()
    check.close()

    # Test for nested YML files with JSON output
    check = open('tests/fixtures/outputs/yml_nest_json.txt',
                 'r', encoding='UTF-8')
    diff = generate_diff(to_json('tests/fixtures/inputs/nest_input.yml'),
                         to_json('tests/fixtures/inputs/nest_output.yml'))
    assert format_diff(diff, 'json') == check.read()
    check.close()

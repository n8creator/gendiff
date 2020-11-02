from gendiff.generate_diff import generate_diff


def test_diff_json():
    """Simple test for flat JSON files."""
    check = open('tests/fixtures/diff_json.txt', 'r', encoding='UTF-8')
    assert generate_diff('tests/fixtures/input.json',
                         'tests/fixtures/output.json') == check.read()
    check.close()


def test_diff_yml():
    """Simple test for foat YML/YAML files."""
    check = open('tests/fixtures/diff_yml.txt', 'r', encoding='UTF-8')
    assert generate_diff('tests/fixtures/input.yml',
                         'tests/fixtures/output.yml') == check.read()
    check.close()

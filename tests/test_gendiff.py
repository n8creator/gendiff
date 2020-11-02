from gendiff.generate_diff import generate_diff


def test_diff_json():
    """Simple test for flat JSON files."""
    check = open('tests/fixtures/diff_json.txt', 'r', encoding='UTF-8')
    assert generate_diff('tests/fixtures/input.json',
                         'tests/fixtures/output.json') == check.read()
    check.close()

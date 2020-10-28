from gendiff.generate_diff import generate_diff


def test_diff_json():
    """Simple test for flat JSON files."""
    check = open('tests/fixtures/result.txt', 'r', encoding='UTF-8')
    assert generate_diff('tests/fixtures/file1.json',
                         'tests/fixtures/file2.json') == check.read()
    check.close()

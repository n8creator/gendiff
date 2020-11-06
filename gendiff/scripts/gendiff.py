"""Gendiff Script."""
import argparse
from gendiff import generate_diff
from gendiff.file_to_json import file_to_json
import json


def main():
    """Generate Difference Main Script.

    Function takes two JSON files as arguments, and calls generate_diff()
    function to find the difference between them.
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()

    # Converting function agruments to .json format
    input, output = file_to_json(args.first_file),\
        file_to_json(args.second_file)

    diff = generate_diff(input, output)
    print(json.dumps(diff, indent=4, sort_keys=True))


if __name__ == '__main__':
    main()

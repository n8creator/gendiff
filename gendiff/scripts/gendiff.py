"""Gendiff Script."""
import argparse
from gendiff.generate_diff import generate_diff


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
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()

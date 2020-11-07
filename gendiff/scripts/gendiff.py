"""Gendiff Executable Script That Will Be Installed When Installing Package."""
from gendiff.args_parser import parse_args
from gendiff.to_json_converter import file_to_json
from gendiff.generate_diff import generate_diff
from gendiff.format_diff import format_diff


def main():
    # Parse args and append them to variables
    args = parse_args()
    input, output, format = args.first_file, args.second_file, args.format

    # Converting agruments to .json format
    input, output = file_to_json(input), file_to_json(output)

    # Generating diff between input & output files
    diff = generate_diff(input, output)

    # Return formatted diff
    print(format_diff(diff, format))


if __name__ == '__main__':
    main()

"""Gendiff Executable Script That Will Be Installed When Installing Package."""
from gendiff.args_parser import parse_args
from gendiff.format_diff import formatted_diff


def main():
    # Parsing arguments and appending them to variables
    args = parse_args()

    # Returning formatted diff with 'format' argument specified by user
    print(formatted_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()

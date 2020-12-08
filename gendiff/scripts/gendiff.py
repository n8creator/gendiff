"""Gendiff Executable Script That Will Be Installed When Installing Package."""
from gendiff.args_parser import parse_args
from gendiff import generate_diff


def main():
    # Parsing arguments and appending them to variables
    args = parse_args()

    # Returning formatted diff with 'format' argument specified by user
    print(generate_diff(file_path_1=args.first_file,
                        file_path_2=args.second_file,
                        format=args.format))


if __name__ == '__main__':
    main()

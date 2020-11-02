"""Generate Difference Module."""
import re
from gendiff.file_to_json import file_to_json


def generate_diff(file_path1, file_path2):
    """Generate Difference Function.

    Function accepts two .json files (input file and output file), and
    finds the difference between keys and values in these files.

    Args:
        file_path1 ([file]): input file (contains the original data)
        file_path2 ([file]): output file (contains modified data)

    Returns:
        [string]: formatted string
    """

    # Converting files to .json format
    input, output = file_to_json(file_path1), file_to_json(file_path2)

    # Comparing two dictionaries to find differences
    deleted = set(input.items()) - set(output.items())
    added = set(output.items()) - set(input.items())
    unchanged = set(output.items()) & set(input.items())

    # Converting sets() to dicts{}
    deleted, added, unchanged = dict(deleted), dict(added), dict(unchanged)

    # Saving results into output[] list
    output = []

    for key, value in deleted.items():
        output.append('   - {0}: {1}'.format(key, value))
    for key, value in added.items():
        output.append('   + {0}: {1}'.format(key, value))
    for key, value in unchanged.items():
        output.append('   {0}: {1}'.format(key, value))

    # Sorting list by key (key is left part of string before colon)
    # without first arithmetic sign
    output = sorted(output,
                    key=lambda item: re.search(r'[\w\d]*\:', item).group())

    # Adding opening and closing brackets to list
    output.insert(0, '{')
    output.append('}')

    # Returning result
    return "\n".join(output)

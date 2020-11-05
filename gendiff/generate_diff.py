"""Generate Difference Module."""
import re
from gendiff.file_to_json import file_to_json


def generate_diff(file_path1, file_path2):
    """Generate Difference Function.

    Function accepts two files (input file and output file), and
    finds the difference between keys and values in these files.

    Args:
        file_path1 ([file]): input file (contains the original data)
        file_path2 ([file]): output file (contains modified data)

    Returns:
        [string]: formatted string
    """

    # Converting function agruments to .json format
    input, output = file_to_json(file_path1), file_to_json(file_path2)

    # Comparing input and output dict's to find difference between keys
    deleted = input.keys() - output.keys()
    added = output.keys() - input.keys()
    intersected = input.keys() & output.keys()

    # Saving deleted and added items into difference[] list
    difference = []

    for key in deleted:
        difference.append('   - {0}: {1}'.format(key, input[key]))
    for key in added:
        difference.append('   + {0}: {1}'.format(key, output[key]))

    # Saving unchanged & changed items into difference[] list
    for key in intersected:
        if input[key] == output[key]:
            difference.append('   {0}: {1}'.format(key, input[key]))
        else:
            difference.append('   - {0}: {1}'.format(key, input[key]))
            difference.append('   + {0}: {1}'.format(key, output[key]))

    # Sorting difference[] list by key (key here is left part of string
    # before colon without first arithmetic sign and space sign after it)
    difference = sorted(difference,
                        key=lambda item: re.search(r'[\w\d]*\:', item).group())

    # Adding opening and closing brackets to list
    difference.insert(0, '{')
    difference.append('}')

    # Returning result
    return "\n".join(difference)

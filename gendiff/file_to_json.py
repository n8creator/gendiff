"""File converter to .json format"""
import json
import os
import yaml
SUFFIX = -1


def file_to_json(file_path):
    """Convert file to .json format.

    Function accepts some input file with .json, .yml or .yaml extension
    and returns .json formatted file.

    Args:
        file_path ([type]): input file (.json, .yml, .yaml extensions suported)

    Returns:
        json: function returns .json file
    """
    # Getting file extension for later usage if-else statement
    file_extension = os.path.splitext(file_path)[SUFFIX]

    # Processing files with .json extension
    if file_extension == '.json':
        output = json.load(open(file_path))

    # Processing files with .yml or .yaml extension
    elif file_extension == '.yml' or '.yaml':
        with open(file_path) as file:
            file_data = yaml.safe_load(file)
            json_string = json.dumps(file_data)
            output = json.loads(json_string)

    return output

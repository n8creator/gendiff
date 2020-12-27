"""Module Converting File to Dict."""
import json
import os
import yaml


def data_loader(file, file_extension):
    """Function loads file and processes it depending on the extension.

    Args:
        file ([json, yml, yaml]): input file
        file_extension ([string]): file extension

    Raises:
        ValueError: message about unsupported file

    Returns:
        [dict]: function returns dict file
    """
    # Processing files with .json extension
    if file_extension == '.json':
        return json.load(file)

    # Processing files with .yml or .yaml extension
    elif file_extension == '.yml' or '.yaml':
        return yaml.safe_load(file)

    # Raise Error for Unsupported Files
    raise ValueError(
        (f'Selected file with {file_extension} extension format unsupported.'
         f'Please select file in ".json" or ".yml/.yaml" format')
    )


def to_dict(file_path):
    """Convert file to dict{} format.

    Function accepts some input file with .json, .yml or .yaml extension
    and returns data as a dict.

    Args:
        file_path ([json, yml, yaml]): input file

    Returns:
        dict: function returns dictionary
    """

    # Getting file extension
    _, file_extension = os.path.splitext(file_path)

    # Loading data as a dict
    with open(file_path) as file:
        return data_loader(file, file_extension)

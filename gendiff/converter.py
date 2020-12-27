"""Module Converting File to Dict."""
import os
from gendiff.parser import parse_data


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
        return parse_data(file, file_extension)

"""Module Converting Input File into Dict."""
from gendiff.parser import parse_data
from gendiff.loader import load_data


def to_dict(file_path):
    """Convert file to Python's dict.

    Function accepts some input file with .json, .yml or .yaml extension
    and returns data as a Python's dict.

    Args:
        file_path ([json, yml, yaml]): input file

    Returns:
        dict: function returns Python's dict
    """

    # Load file data
    data, extension = load_data(file_path)

    # Return Python's dict
    return parse_data(data, extension)

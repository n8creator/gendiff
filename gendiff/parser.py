"""Module Loading Data."""
import json
import yaml


def parse_data(file, file_extension):
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

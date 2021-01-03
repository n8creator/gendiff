"""Module Parsing Data."""
import json
import yaml

LOADERS = {
    '.yaml': yaml.safe_load,
    '.yml': yaml.safe_load,
    '.json': json.loads
}


def parse_data(data, file_extension):
    """Function loads file data and processes it depending on the extension.

    Args:
        data ([string]): string file data
        file_extension ([string]): file extension

    Raises:
        ValueError: message about unsupported file format

    Returns:
        [dict]: function returns python dict file
    """

    # Parse data if file format contains in LOADERS dict
    if file_extension in LOADERS.keys():
        return LOADERS.get(file_extension)(data)

    # Raise Error for unsupported file formats
    raise ValueError(
        (f'Selected file with {file_extension} extension format unsupported.'
         f'Please select file in ".json" or ".yml/.yaml" format')
    )

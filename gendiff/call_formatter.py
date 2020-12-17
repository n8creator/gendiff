"""Select Formatter Module."""
from gendiff.formatters.stylish import render as render_stylish
from gendiff.formatters.plain import render_plain
from gendiff.formatters.json import render_json


FORMATS = {
    'json': render_json,
    'plain': render_plain,
    'stylish': render_stylish
}

DEFAULT_FORMAT = 'stylish'


def format_tree(diff, format):
    """Function returns formatted tree depending on the option specified by
    the user.

    Args:
        diff ([json]): generated json file with difference between first and
                       second comparable files
        format ([string]): option specified by user in CLI interface

    Returns:
        [json, string]: returns string or json depending of user
                        specified format
    """

    if format is None:
        format = DEFAULT_FORMAT

    if format in FORMATS.keys():
        return FORMATS.get(format)(diff)
    else:
        return RuntimeError('ERROR: Style is not supported')

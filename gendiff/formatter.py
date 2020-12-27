"""Module Selecting Formatter."""
from gendiff.formatters.stylish import render as render_stylish
from gendiff.formatters.plain import render as render_plain
from gendiff.formatters.json import render as render_json


JSON, PLAIN, STYLISH = 'json', 'plain', 'stylish'
FORMATS = {
    JSON: render_json,
    PLAIN: render_plain,
    STYLISH: render_stylish
}


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
        format = STYLISH

    if format in FORMATS.keys():
        return FORMATS.get(format)(diff)
    else:
        return RuntimeError(f'ERROR: format "{format}" is not supported')

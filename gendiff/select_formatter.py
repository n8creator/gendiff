"""Select Formatter Module."""
from gendiff.formatters.stylish import render_stylish
from gendiff.formatters.plain import render_plain
from gendiff.formatters.json import render_json


def formatter(diff, format):
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

    if format:
        if format.lower() == 'json':
            return render_json(diff)
        elif format.lower() == 'plain':
            return render_plain(diff)
        elif format.lower() == 'stylish':
            return render_stylish(diff)
    else:
        return render_stylish(diff)

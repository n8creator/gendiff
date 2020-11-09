from gendiff.formatters.stylish import render
from gendiff.formatters.plain import render_plain
from gendiff.formatters.json import render_json


def format_diff(diff, format=None):
    if format:
        if format.lower() == 'json':
            return render_json(diff)
        elif format.lower() == 'plain':
            return render_plain(diff)
    else:
        return render(diff)

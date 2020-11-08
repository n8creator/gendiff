from gendiff.formatters.stylish import render
from gendiff.formatters.plain import render_plain


def format_diff(diff, format=None):
    if format:
        if format.lower() == 'json':
            return render(diff)
        elif format.lower() == 'plain':
            return render_plain(diff)
    else:
        return render(diff)

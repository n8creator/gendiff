from gendiff.formatters.stylish import render


def format_diff(diff, format=None):
    if format:
        if format.lower() == 'json':
            return(render(diff))
        elif format.lower() == 'plain':
            return(render(diff))
    else:
        return(render(diff))

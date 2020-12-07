from gendiff.to_json_converter import to_json
from gendiff.generate_diff import generate_difference
from gendiff.formatters.stylish import render
from gendiff.formatters.plain import render_plain
from gendiff.formatters.json import render_json


def formatted_diff(input, output, format=None):
    # Converting agruments to .json (input & output now has dict{} formats)
    input, output = to_json(input), to_json(output)

    # Generating difference tree
    diff = generate_difference(input, output)

    # Returning formatted tree depending on the format specified by the user
    if format:
        if format.lower() == 'json':
            return render_json(diff) + '\n'
        elif format.lower() == 'plain':
            return render_plain(diff) + '\n'
    else:
        return render(diff) + '\n'

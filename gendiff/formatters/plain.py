from gendiff.generate_diff import ADDED, DELETED, NESTED, CHANGED

# OLD_VAL and NEW_VAL are indexes for dicts containing replaced value (OLD_VAL)
# and new one (NEW_VAL).They are used to get rid of "magic numbers" in the code
OLD_VAL, NEW_VAL = (0, 1)


def format_value(text):
    """Function formatting string text to match expected output

    Args:
        var ([any]): any text variable

    Returns:
        [str]: formatted text
    """

    if isinstance(text, dict):
        return '[complex value]'
    elif isinstance(text, int):
        return int(text)
    elif text == 'true':
        return 'true'
    elif text == 'false':
        return 'false'
    elif text == 'null':
        return 'null'
    else:
        return f'\'{text}\''


def render_plain_engine(diff, path):
    # Initialize output variable
    output = []

    for key, data in sorted(diff.items()):
        # Generate path from the root as a plain string
        root_path = f'{path}.{key}' if path else key

        # diff_dict traversal
        if data['type'] == NESTED:
            output.append(render_plain_engine(data['values'],
                                              root_path)
                          )
        elif data['type'] == ADDED:
            output.append(f'Property \'{root_path}\' was added with '
                          + f'value: {format_value(data["values"])}')
        elif data['type'] == DELETED:
            output.append(f'Property \'{root_path}\' was removed')
        elif data['type'] == CHANGED:
            output.append(f'Property \'{root_path}\' was updated. From '
                          + f'{format_value(data["values"][OLD_VAL])} to '
                          + f'{format_value(data["values"][NEW_VAL])}')

    # Return output as a string
    return '\n'.join(output)


def render_plain(diff):
    return (render_plain_engine(diff, path=None))

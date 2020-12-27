from gendiff.tree import ADDED, DELETED, NESTED, CHANGED


def to_string(value):
    """Function formatting input value to match expected text output

    Args:
        var ([any]): any value variable

    Returns:
        [str]: formatted text
    """

    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return 'true' if value is True else 'false'
    elif isinstance(value, int):
        return int(value)
    elif value is None:
        return 'null'
    else:
        return f'\'{value}\''


def render_diff(diff, path):
    # Initialize output variable
    output = []

    for key, data in sorted(diff.items()):
        # Generate path from the root as a plain string
        root_path = f'{path}.{key}' if path else key

        # diff_dict traversal
        if data['type'] == NESTED:
            output.append(render_diff(data['values'],
                                      root_path)
                          )
        elif data['type'] == ADDED:
            output.append((f'Property \'{root_path}\' was added with '
                           f'value: {to_string(data["values"])}'))
        elif data['type'] == DELETED:
            output.append(f'Property \'{root_path}\' was removed')
        elif data['type'] == CHANGED:
            (old_value, new_value) = data["values"]
            output.append((f'Property \'{root_path}\' was updated. From '
                           f'{to_string(old_value)} to '
                           f'{to_string(new_value)}'))

    # Return output as a string
    return '\n'.join(output)


def render(diff):
    return (render_diff(diff, path=None))

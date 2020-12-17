from gendiff.build_tree import ADDED, DELETED, NESTED, CHANGED

# OLD_VAL and NEW_VAL are indexes for dicts containing replaced value (OLD_VAL)
# and new one (NEW_VAL).They are used to get rid of "magic numbers" in the code
OLD_VAL, NEW_VAL = (0, 1)


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
        if value is True:
            return 'true'
        elif value is False:
            return 'false'
    elif isinstance(value, int):
        return int(value)
    elif value is None:
        return 'null'
    else:
        return f'\'{value}\''


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
            output.append((f'Property \'{root_path}\' was added with '
                           f'value: {to_string(data["values"])}'))
        elif data['type'] == DELETED:
            output.append(f'Property \'{root_path}\' was removed')
        elif data['type'] == CHANGED:
            output.append((f'Property \'{root_path}\' was updated. From '
                           f'{to_string(data["values"][OLD_VAL])} to '
                           f'{to_string(data["values"][NEW_VAL])}'))

    # Return output as a string
    return '\n'.join(output)


def render_plain(diff):
    return (render_plain_engine(diff, path=None))

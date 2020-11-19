from gendiff.generate_diff import ADDED, DELETED, NESTED, CHANGED

OLD_VAL, NEW_VAL = 0, 1


def generate_plain_string(key, value, type, replaced_value="None"):
    # Formatting input data to use in output
    value = '[complex value]' if isinstance(value, dict) else\
        '\'{0}\''.format(value)
    replaced_value = '[complex value]' if isinstance(replaced_value, dict)\
        else '\'{0}\''.format(replaced_value)
    key = '\'{0}\''.format(key)

    # Code below returns formatted strings
    if type == ADDED:
        return 'Property {0} was added with value: {1}\n'.\
            format(key, value)
    elif type == DELETED:
        return 'Property {0} was removed\n'.format(key)
    elif type == CHANGED:
        return 'Property {0} was updated. From {1} to {2}\n'.\
            format(key, value, replaced_value)


def render_plain_engine(diff, path):
    # Initialize output variable
    output = ''

    for key, data in sorted(diff.items()):
        # Generate path from the root as a plain string
        root_path = '{0}.{1}'.format(path, key) if path else key

        # diff_dict traversal
        if data['type'] == NESTED:
            output += render_plain_engine(data['values'], root_path) + '\n'
        elif data['type'] == ADDED:
            output += generate_plain_string(root_path,
                                            data['values'],
                                            ADDED)
        elif data['type'] == DELETED:
            output += generate_plain_string(root_path,
                                            data['values'],
                                            DELETED)
        elif data['type'] == CHANGED:
            output += generate_plain_string(root_path,
                                            data['values'][OLD_VAL],
                                            CHANGED,
                                            data['values'][NEW_VAL])

    # Return output without empty rows
    return output.strip('\n')


def render_plain(diff):
    return render_plain_engine(diff, path=None)

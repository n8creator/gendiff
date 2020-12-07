from gendiff.generate_diff import ADDED, DELETED, NESTED, CHANGED, UNMODIFIED

SPACE = 4
OLD_VAL, NEW_VAL = 0, 1

SIGN_CONVERTER = {
    NESTED: None,
    UNMODIFIED: None,
    ADDED: '+',
    DELETED: '-'
}


def formatter(type, value, spaces, sign=None):
    left_indent = '' + (' ' * spaces)
    if not sign:
        sign = ' '
    output = f'{left_indent}{sign} {type}: {value}\n'
    return output


def nest_formatter(dict_, spaces):
    # Destructuring dict to key & value variables
    key, value = next(iter(dict_.items()))

    row_indent = ' ' * spaces
    blank_indent = ' ' * (spaces - 2)  # Removes 2 chars: (+/-) and space
    output = f"{{\n  {row_indent}{key}: {value}\n{blank_indent}}}"
    return output


def render_engine(diff, spaces):
    # Initialize output list
    output = []
    output.append('{\n')

    # Iterate diff_dict
    for type, node in diff.items():

        # If node type has NESTED type then we put node value in
        # render_engine() function and call it recursively
        if node['type'] == NESTED:
            output.append(formatter(type,
                                    render_engine(
                                        node['values'],
                                        spaces=spaces+SPACE),
                                    spaces))

        # If node has dict type but not equals CHANGED nor NESTED, that means
        # node may belong to ADDED, DELETED or UNMODIFIED type.
        # In this case we need to format node by appending spaces and
        # arithmetic sign in output string (before node type)
        elif not node['type'] == CHANGED and isinstance(node['values'], dict):
            output.append(formatter(type,
                                    render_engine(
                                        node['values'],
                                        spaces=spaces+SPACE),
                                    spaces,
                                    sign=SIGN_CONVERTER[node['type']]))

        # If node has CHANGED type, these changes could have been made in
        # three ways
        elif node['type'] == CHANGED:

            # Case 1: OLD value is dict and NEW value is not
            if isinstance(node['values'][OLD_VAL], dict) and\
                          not isinstance(node['values'][NEW_VAL], dict):
                output.append(formatter(type,
                                        nest_formatter(
                                            node['values'][OLD_VAL],
                                            spaces=spaces+SPACE),
                                        spaces=spaces,
                                        sign='-'))
                output.append(formatter(type, node['values'][NEW_VAL],
                                        spaces=spaces, sign='+'))

            # Case 2: NEW value is dict and OLD value is not
            elif not isinstance(node['values'][OLD_VAL], dict) and\
                    isinstance(node['values'][NEW_VAL], dict):
                output.append(formatter(type, node['values'][OLD_VAL],
                                        spaces=spaces, sign='-'))
                output.append(formatter(type, nest_formatter(
                                                node['values'][NEW_VAL],
                                                spaces=spaces+SPACE
                                                ),
                                        spaces=spaces,
                                        sign='+'))

            # Case 3: Both NEW & OLD values are not dict's
            else:
                output.append(formatter(type, node['values'][OLD_VAL],
                                        spaces=spaces, sign='-'))
                output.append(formatter(type, node['values'][NEW_VAL],
                                        spaces=spaces, sign='+'))

        # Any other cases (if node has been ADDED, DELETED or UNMODIFIED)
        else:
            output.append(formatter(type, node['values'],
                                    spaces=spaces,
                                    sign=SIGN_CONVERTER[node['type']]))

    # Returning output
    output.append(' ' * (spaces-2) + '}')
    return ''.join(output)


def render(diff):
    return render_engine(diff, spaces=2) + '\n'

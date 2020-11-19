"""Generate Difference Module."""

ADDED, DELETED, NESTED = 'added', 'deleted', 'nested'
UNMODIFIED, CHANGED = 'unmodified', 'changed'


def to_string(value):
    """System Keyword to String Converter.

    Function accept some value, and checks if this value belong to a system
    value. In True case function return system value formatted as string,
    otherwise function returns value "as it is" without any formatting.

    Args:
        value ([string, dict, bool, None]): any value

    Returns:
        value ([string, dict]): formatted value
    """

    # Values dict needed to be converted
    converter = {
        None: 'null',
        False: 'false',
        True: 'true'
    }

    if not isinstance(value, dict) and value in converter:
        return converter[value]
    else:
        return value


def generate_difference(input, output):
    """Generate Difference Function.

    Function accepts two dicts (input and output), and finds
    the difference between keys and values in those dicts.

    Args:
        input ([dict]): input dict (contains original data)
        output ([dict]): output dict (contains modified data)

    Returns:
        difference ([dict]): output dict containing difference
                             between input & output dicts
    """

    # Comparing input and output dict's to find differences between keys
    intersected = input.keys() & output.keys()
    deleted = input.keys() - output.keys()
    added = output.keys() - input.keys()

    # Initializing variable containing function output
    difference = {}

    # Traversing each element of the tree
    for key in intersected:
        input_value, output_value = input[key], output[key]

        if isinstance(input_value, dict) and isinstance(output_value, dict):
            difference[key] = ({'type': NESTED,
                                'values': generate_difference(input_value,
                                                              output_value)
                                })
        elif input_value == output_value:
            difference[key] = ({'type': UNMODIFIED,
                               'values': to_string(input_value)})
        else:
            difference[key] = ({'type': CHANGED,
                                'values': (to_string(input_value),
                                           to_string(output_value)
                                           )
                                })

    for key in added:
        values = output[key]
        if type(values) == dict:
            difference[key] = ({'type': ADDED,
                                'values': generate_difference(values, values)
                                })
        else:
            difference[key] = ({'type': ADDED, 'values': to_string(values)})

    for key in deleted:
        values = input[key]
        if type(values) == dict:
            difference[key] = ({'type': DELETED,
                                'values': generate_difference(values, values)
                                })
        else:
            difference[key] = ({'type': DELETED, 'values': to_string(values)})

    # Returning function output
    return difference

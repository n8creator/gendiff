"""Generate Difference Module."""

ADDED, DELETED, NESTED = 'added', 'deleted', 'nested'
UNMODIFIED, CHANGED = 'unmodified', 'changed'


def generate_diff(input, output):
    """Generate Difference Function.

    Function accepts two dicts (input and output), and finds
    the difference between keys and values in those dicts.

    Args:
        input ([dict]): input dict (contains the original data)
        output ([dict]): output dict (contains modified data)

    Returns:
        differenct ([dict]): analyzed dict
    """

    # Comparing input and output dict's to find differences between keys
    intersected = input.keys() & output.keys()
    deleted = input.keys() - output.keys()
    added = output.keys() - input.keys()

    # Initializing variable containing function output
    difference = {}

    for key in intersected:
        input_value, output_value = input[key], output[key]

        if isinstance(input_value, dict) and isinstance(output_value, dict):
            difference[key] = ({'type': NESTED,
                                'values': generate_diff(input_value,
                                                        output_value)
                                })
        elif input_value == output_value:
            difference[key] = ({'type': UNMODIFIED,
                               'values': input_value})
        else:
            difference[key] = ({'type': CHANGED,
                                'values': (input_value, output_value)})

    for key in added:
        values = output[key]
        if type(values) == dict:
            difference[key] = ({'type': ADDED,
                                'values': generate_diff(values, values)
                                })
        else:
            difference[key] = ({'type': ADDED, 'values': values})

    for key in deleted:
        values = input[key]
        if type(values) == dict:
            difference[key] = ({'type': DELETED,
                                'values': generate_diff(values, values)
                                })
        else:
            difference[key] = ({'type': DELETED, 'values': values})

    # Returning function output
    return difference

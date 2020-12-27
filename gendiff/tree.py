"""Build Difference Tree Module."""

from collections import OrderedDict

ADDED, DELETED, NESTED = 'added', 'deleted', 'nested'
UNMODIFIED, CHANGED = 'unmodified', 'changed'


def get_ordered_joint_keys(dict1, dict2):
    """Function compares 2 dictionaries and returns joint keys (keys list may
    be sorted or unsorted)

    Args:
        dict1 ([dict]): first dictionary
        dict2 ([dict]): second dictionary

    Returns:
        [list]: if both comparable dictionaries are not empty and not equal,
                function returns list of joint keys sorted alphabetically.
                In case when one of the dictionary is empty or both of them
                are equal, function returns list list of keys "as is"
                (in original order).
    """

    # Initializing output list
    output_list = []

    # Adding sorted keys from dict1 & dict2 into output list
    for key in OrderedDict(dict1):
        output_list.append(key)

    for key in OrderedDict(dict2):
        if key not in output_list:
            output_list.append(key)

    # If one of the dict1 or dict2 is empty, or both dicts are equal
    # return output unsorted
    if (not dict1 or not dict2) or (dict1 == dict2):
        return output_list
    # otherwise return sorted list
    else:
        return sorted(output_list)


def build_diff(input, output):
    """Generate Difference Function.

    Function accepts two dicts (input and output), and discovers
    the difference between keys and values in those dicts.

    Args:
        input ([dict]): input dict (contains original data)
        output ([dict]): output dict (contains modified data)

    Returns:
        difference ([dict]): output dict containing difference
                             between input & output dicts
    """

    # Getting list of joint keys from input & output files
    joint = get_ordered_joint_keys(input, output)

    # Comparing input and output dict's to find differences between keys
    intersected = input.keys() & output.keys()
    deleted = input.keys() - output.keys()
    added = output.keys() - input.keys()

    # Initializing variable containing function output
    difference = {}

    # Traversing each element of the tree
    for key in joint:
        if key in intersected:
            input_val, output_val = input[key], output[key]

            if isinstance(input_val, dict) and isinstance(output_val, dict):
                difference[key] = {'type': NESTED,
                                   'values': build_diff(input_val,
                                                        output_val)
                                   }
            elif input_val == output_val:
                difference[key] = {'type': UNMODIFIED,
                                   'values': input_val}
            else:
                difference[key] = {'type': CHANGED,
                                   'values': (input_val,
                                              output_val
                                              )
                                   }

        if key in added:
            values = output[key]
            if type(values) == dict:
                difference[key] = {'type': ADDED,
                                   'values': build_diff(values,
                                                        values)
                                   }
            else:
                difference[key] = {'type': ADDED,
                                   'values': values}

        if key in deleted:
            values = input[key]
            if type(values) == dict:
                difference[key] = {'type': DELETED,
                                   'values': build_diff(values,
                                                        values)
                                   }
            else:
                difference[key] = {'type': DELETED,
                                   'values': values}

    # Returning function output
    return difference

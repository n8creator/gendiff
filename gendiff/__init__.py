from gendiff.converter import to_dict
from gendiff.tree import build_diff
from gendiff.formatter import format_tree


def generate_diff(file_path_1, file_path_2, format):

    # Converting agruments to .json dicts and Generating difference tree
    diff = build_diff(to_dict(file_path_1),
                      to_dict(file_path_2))

    # Return formatted tree
    return format_tree(diff, format)


__all__ = ('generate_diff', )

from gendiff.to_dict_converter import to_dict
from gendiff.build_tree import build_diff_tree
from gendiff.select_formatter import format_tree


def generate_diff(file_path_1, file_path_2, format=None):

    # Converting agruments to .json dicts and Generating difference tree
    diff = build_diff_tree(to_dict(file_path_1),
                           to_dict(file_path_2))

    # Return formatted tree
    return format_tree(diff, format)


__all__ = ('generate_diff', )

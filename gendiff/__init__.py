from gendiff.to_json_converter import to_json
from gendiff.build_tree import build_diff_tree
from gendiff.select_formatter import formatter


def generate_diff(file_path_1, file_path_2, format=None):

    # Converting agruments to .json dicts and Generating difference tree
    diff = build_diff_tree(to_json(file_path_1),
                           to_json(file_path_2))

    return formatter(diff, format)


__all__ = ('generate_diff', )

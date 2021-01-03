"""Module Loading Data."""
import os


def load_data(file_path):
    """Function loading file data as a string.

    Args:
        file_path ([file]): any input file

    Returns:
        [tuple]: returns tuple containing file data as a string
                 and file extension
    """

    # Getting file extension
    _, file_extension = os.path.splitext(file_path)

    # Loading data into variable
    with open(file_path, 'r') as file:
        data = file.read()

    # Return tuple containing `string` data and file extension
    return (data, file_extension)

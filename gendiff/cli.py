import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        default=None,
                        help='set format of output (leave blank or\
                              select "json" or "plain" format)')
    args = parser.parse_args()
    return args

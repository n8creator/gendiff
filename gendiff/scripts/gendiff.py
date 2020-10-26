import argparse

parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
args = parser.parse_args()

def main():
    print("This is a Gendiff project!")

if __name__ == '__main__':
    main()
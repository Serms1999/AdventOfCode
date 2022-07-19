import os
import sys


def read_input_lines():
    current_input = os.path.join(os.getcwd(), 'input')
    try:
        with open(current_input, 'r') as input_file:
            lines = input_file.read().splitlines()
    except FileNotFoundError:
        print(f'No such file or directory: \'{current_input}\'', file=sys.stderr)
        sys.exit(1)

    return lines

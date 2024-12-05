import os
import sys
import inspect

from typing import List, Optional


def read_input_lines(file_name: str ='input') -> List[str]:
    caller_file = inspect.getouterframes(inspect.currentframe(), 2)[1][1]
    current_path = os.path.dirname(caller_file)
    file_path = os.path.join(current_path, file_name)
    try:
        with open(file_path, 'r') as input_file:
            return input_file.read().splitlines()
    except FileNotFoundError:
        print(f'No such file or directory: \'{file_path}\'', file=sys.stderr)
        sys.exit(1)

def format_output(output_part1: str, output_part2: Optional[str] = None) -> None:
    fill_number: int = max(len(output_part1), len(output_part2)) if output_part2 is not None else len(output_part1)
    fill_number = (fill_number - len(' Part X ') + 1) // 2
    print(f'{"-" * fill_number} Part 1 {"-" * fill_number}')
    print(output_part1)
    if output_part2 is not None:
        print(f'{"-" * fill_number} Part 2 {"-" * fill_number}')
        print(output_part2)
    print(f'{"-" * (fill_number * 2 + len(" Part X "))}')

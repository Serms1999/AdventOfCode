from pathlib import Path
from sys import stderr, exit
import inspect


def read_input_lines(file_name: str ='input') -> list[str]:
    caller_file = inspect.getouterframes(inspect.currentframe(), 2)[1][1]
    current_path: Path = Path(caller_file).parent
    file_path: Path = current_path / file_name
    try:
        with open(file_path, 'r') as input_file:
            return input_file.read().splitlines()
    except FileNotFoundError:
        print(f'No such file or directory: \'{file_path}\'', file=stderr)
        exit(1)
    return []

def format_output(output_part1: str, output_part2: str | None = None) -> None:
    fill_number: int = max(len(output_part1), len(output_part2)) if output_part2 is not None else len(output_part1)
    fill_number = (fill_number - len(' Part X ') + 1) // 2
    print(f'{"-" * fill_number} Part 1 {"-" * fill_number}')
    print(output_part1)
    if output_part2 is not None:
        print(f'{"-" * fill_number} Part 2 {"-" * fill_number}')
        print(output_part2)
    print(f'{"-" * (fill_number * 2 + len(" Part X "))}')

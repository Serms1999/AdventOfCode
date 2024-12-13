from IO import read_input_lines, format_output
from itertools import repeat
from unittest import TestCase, TestResult, TestLoader, TextTestRunner


class PartialTests(TestCase):
    def test_part1(self):
        self.assertEqual(get_filesystem_checksum(list(read_input_lines(file_name='test_input')[0])), 1928)

    def test_part2(self):
        self.assertEqual(get_filesystem_checksum_whole_files(list(read_input_lines(file_name='test_input')[0])), 2858)


def get_filesystem_checksum(encoded_file_system: list[str]) -> int:
    file_system: list[int | str] = []
    current_id: int = 0

    for index, block in enumerate(encoded_file_system):
        times: int = int(block)
        item: int | str
        if index % 2 == 0:
            item = current_id
            current_id += 1
        else:
            item = '.'
        file_system.extend(repeat(item, times))

    index1: int
    index2: int
    index1, index2 = 0, len(file_system) - 1

    while index1 < index2:
        while file_system[index1] != '.' and index1 < index2:
            index1 += 1

        while file_system[index2] == '.' and index1 < index2:
            index2 -= 1

        if index1 < index2 and file_system[index1] == '.' and file_system[index2] != '.':
            file_system[index1], file_system[index2] = file_system[index2], file_system[index1]

    index: int = 0
    value: int | str  = file_system[0]
    checksum: int = 0
    while index < index1:
        checksum += value * index
        index += 1
        value = file_system[index]

    return checksum


class FreeSpace:
    def __init__(self, index: int, size: int) -> None:
        self.first_index: int = index
        self.size: int = size

    def last_index(self) -> int:
        return self.first_index + self.size - 1

    def __repr__(self) -> str:
        return f'Free Space ({self.first_index}, {self.last_index()})'

    def __str__(self) -> str:
        return f'Free Space: indexes {self.first_index} to {self.last_index()}'


class File(FreeSpace):
    def __init__(self, file_id: int, index: int, size: int) -> None:
        super().__init__(index, size)
        self.file_id: int = file_id

    def __repr__(self) -> str:
        return f'File {self.file_id} ({self.first_index}, {self.last_index()})'

    def __str__(self) -> str:
        return f'File {self.file_id}: indexes {self.first_index} to {self.last_index()}'


def get_filesystem_checksum_whole_files(encoded_file_system: list[str]) -> int:
    def filesystem_str() -> str:
        all_blocks: list[FreeSpace | File] = []
        all_blocks.extend(files)
        all_blocks.extend(free_spaces)
        all_blocks.sort(key=lambda x: x.first_index)

        result: str = ''
        for filesystem_block in all_blocks:
            if filesystem_block.size == 0:
                continue
            if isinstance(filesystem_block, File):
                result += f'{str(filesystem_block.file_id) * filesystem_block.size}'
            else:
                result += '.' * filesystem_block.size
        return result


    def combine_free_spaces() -> list[FreeSpace]:
        free_spaces.sort(key=lambda x: x.first_index)
        space_index: int = 0
        while space_index < len(free_spaces) - 1:
            current_space = free_spaces[space_index]
            next_space = free_spaces[space_index + 1]

            if current_space.size == 0:
                free_spaces.pop(space_index)
            elif current_space.last_index() + 1 == next_space.first_index:
                current_space.size += next_space.size
                free_spaces.pop(space_index + 1)
            else:
                space_index += 1
        return free_spaces


    files: list[File] = []
    free_spaces: list[FreeSpace] = []

    current_id: int = 0
    current_index: int = 0
    for index, block in enumerate(encoded_file_system):
        size: int = int(block)
        if index % 2 == 0:
            files.append(File(file_id=current_id, index=current_index, size=size))
            current_id += 1
        else:
            free_spaces.append(FreeSpace(index=current_index, size=size))
        current_index += size

    for file in reversed(files):
        free_space_index: int = 0
        while free_space_index < len(free_spaces) and file.size > free_spaces[free_space_index].size and free_spaces[free_space_index].last_index() < file.first_index:
            free_space_index += 1

        if free_space_index == len(free_spaces) or free_spaces[free_space_index].last_index() > file.first_index:
            continue

        free_spaces.append(FreeSpace(index=file.first_index, size=file.size))
        file.first_index = free_spaces[free_space_index].first_index
        free_spaces[free_space_index].size -= file.size
        free_spaces[free_space_index].first_index += file.size

        free_spaces = combine_free_spaces()

    checksum: int = 0
    for file in files:
        checksum += sum(file.file_id * file_index for file_index in range(file.first_index, file.last_index() + 1))

    return checksum


def main() -> None:
    result: TestResult = TextTestRunner().run(TestLoader().loadTestsFromTestCase(PartialTests))
    if result.wasSuccessful():
        input_lines: list[str] = read_input_lines(file_name='input')
        format_output(
            output_part1=f'File System Checksum: {get_filesystem_checksum(list(input_lines[0]))}',
            output_part2=f'File System Checksum Whole Files: {get_filesystem_checksum_whole_files(list(input_lines[0]))}'
        )


if __name__ == '__main__':
    main()

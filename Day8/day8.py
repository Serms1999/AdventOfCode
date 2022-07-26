import IO.IO_module as IO


seven_digits_patterns = {
    0: {'a', 'b', 'c', 'e', 'f', 'g'},
    1: {'c', 'f'},
    2: {'a', 'c', 'd', 'e', 'g'},
    3: {'a', 'c', 'd', 'f', 'g'},
    4: {'b', 'c', 'd', 'f'},
    5: {'a', 'b', 'd', 'f', 'g'},
    6: {'a', 'b', 'd', 'e', 'f', 'g'},
    7: {'a', 'c', 'f'},
    8: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
    9: {'a', 'b', 'c', 'd', 'f', 'g'}
}


def check_easy_pattern(value: str) -> bool:
    for n in [1, 4, 7, 8]:
        if len(value) == len(seven_digits_patterns[n]):
            return True

    return False


def get_numbers_by_length(length: int, pattern_list: list) -> list:
    return list(filter(lambda x: len(x) == length, pattern_list))


def part1(lines: list) -> int:
    outputs = [line.split(' | ')[1].split() for line in lines]
    cont = 0
    for output in outputs:
        for value in output:
            if check_easy_pattern(value):
                cont += 1

    return cont


def part2(lines: list) -> int:
    lines_split = [line.split(' | ') for line in lines]

    numbers_sum = 0

    for p, r in lines_split:
        translations = {}
        patterns = p.split()
        results = r.split()

        translations[1] = get_numbers_by_length(2, patterns)[0]
        translations[4] = get_numbers_by_length(4, patterns)[0]
        translations[7] = get_numbers_by_length(3, patterns)[0]
        translations[8] = get_numbers_by_length(7, patterns)[0]

        length_five_patterns = get_numbers_by_length(5, patterns)
        length_six_patterns = get_numbers_by_length(6, patterns)

        for pattern in length_six_patterns:
            if 9 not in translations and set(translations[4]).issubset(set(pattern)):
                translations[9] = pattern
            elif 0 not in translations and set(translations[4]) - set(translations[1]) - set(pattern):
                translations[0] = pattern
            else:
                translations[6] = pattern

        for pattern in length_five_patterns:
            if 3 not in translations and set(translations[1]).issubset(set(pattern)):
                translations[3] = pattern
            elif 5 not in translations and len(set(translations[9]) - set(pattern)) == 1:
                translations[5] = pattern
            else:
                translations[2] = pattern

        translations_sorted_list = []
        for i in range(0, 10):
            translations_sorted_list += [''.join(sorted(list(translations[i])))]

        results_sorted_list = [''.join(sorted(list(number))) for number in results]

        numbers_sum += int(''.join([str(translations_sorted_list.index(result)) for result in results_sorted_list]))

    return numbers_sum


def main():
    input_lines = IO.read_input_lines()
    print(f'Part one solution: {part1(input_lines)}')
    print(f'Part two solution: {part2(input_lines)}')


if __name__ == '__main__':
    main()

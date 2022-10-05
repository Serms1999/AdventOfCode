from IO.IO_module import read_input_lines


current_pairs = {}
letter_count = {}


def read_rules(rules_list: list) -> dict:
    rules = {}
    for line in rules_list:
        pair = line[:2]
        new_letter = line[-1]

        rules[pair] = new_letter

    return rules


def initialize_pairs(template: str) -> None:
    global current_pairs
    current_pairs = {}
    for i in range(0, len(template) - 1):
        pair = template[i:i + 2]
        current_pairs[pair] = letter_count.get(pair, 0) + 1


def initialize_letters(template: str) -> None:
    global letter_count
    letter_count = {}
    for letter in template:
        letter_count[letter] = letter_count.get(letter, 0) + 1


def part1(input_lines: list) -> int:
    global current_pairs, letter_count
    template = input_lines[0]
    rules = read_rules(input_lines[2:])
    initialize_letters(template)
    initialize_pairs(template)

    for _ in range(10):
        aux_dict = {}
        while len(current_pairs) > 0:
            item, value = current_pairs.popitem()
            new_letter = rules[item]
            for new_pair in [f'{item[0]}{new_letter}', f'{new_letter}{item[1]}']:
                aux_dict[new_pair] = aux_dict.get(new_pair, 0) + value

            letter_count[new_letter] = letter_count.get(new_letter, 0) + value

        current_pairs = aux_dict.copy()

    return max(letter_count.values()) - min(letter_count.values())


def part2(input_lines: list) -> int:
    global current_pairs, letter_count
    template = input_lines[0]
    rules = read_rules(input_lines[2:])
    initialize_letters(template)
    initialize_pairs(template)

    for _ in range(40):
        aux_dict = {}
        while len(current_pairs) > 0:
            item, value = current_pairs.popitem()
            new_letter = rules[item]
            for new_pair in [f'{item[0]}{new_letter}', f'{new_letter}{item[1]}']:
                aux_dict[new_pair] = aux_dict.get(new_pair, 0) + value

            letter_count[new_letter] = letter_count.get(new_letter, 0) + value

        current_pairs = aux_dict.copy()

    return max(letter_count.values()) - min(letter_count.values())


def main():
    input_lines = read_input_lines(root_file=__file__)
    print(f'Part one solution: {part1(input_lines)}')
    print(f'Part two solution: {part2(input_lines)}')


if __name__ == '__main__':
    main()

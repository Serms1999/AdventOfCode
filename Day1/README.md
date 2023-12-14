## --- Day 1: Trebuchet?! ---

You try to ask why they can't just use a [weather machine](https://adventofcode.com/2015/day/1) ("not powerful enough")
and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions")
and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves
are already loading you into a [trebuchet](https://en.wikipedia.org/wiki/Trebuchet) ("please hold still, we need to
strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been
**amended** by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are
having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific 
**calibration value** that the Elves now need to recover. On each line, the calibration value can be found by combining
the **first digit** and the **last digit** (in that order) to form a single **two-digit number**.

For example:

```
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
```

In this example, the calibration values of these four lines are `12`, `38`, `15`, and `77`. Adding these together
produces **`142`**.

Consider your entire calibration document. **What is the sum of all of the calibration values?**

<details>
    <summary>Solution</summary>

First, I loop over each line in the input file. Then, I loop over each character in the line. If the character is a
digit, I return it as a string, whereas if it is a letter, I return a empty string. I have two variables, `first_digit`
and `last_digit`, which are initially set to `None`. If `first_digit` is `None`, I set it to the current character, and
then I update `last_digit` to the current number as string.

At the end, I return the integer value of `first_digit` and `last_digit` as a two digit number, and sum them up.

```python
def get_num_or_empty_string(c: str) -> str:
    numbers = '0123456789'
    return c if c in numbers else ''


def map_lines_into_numbers(s: str) -> int:
    first_digit = last_digit = None
    for c in [*s]:
        if str_num := get_num_or_empty_string(c):
            if first_digit is None:
                first_digit = str_num
            last_digit = str_num

    return int(f'{first_digit}{last_digit}')


def get_calibration_sum(lines: list[str]) -> int:
    return sum([map_lines_into_numbers(line) for line in lines])
```
The answer is: `55386`.
</details>


## --- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually **spelled out with letters**: `one`,
`two`, `three`, `four`, `five`, `six`, `seven`, `eight`, and `nine` **also** count as valid "digits".


Equipped with this new information, you now need to find the real first and last digit on each line. For example:



```
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
```

In this example, the calibration values are `29`, `83`, `13`, `24`, `42`, `14`, and `76`. Adding these together produces
**`281`**.


**What is the sum of all of the calibration values?**

<details>
    <summary>Solution</summary>

Here I only have to add a function to convert the spelled numbers into normal numbers and then I have the previous
situation. The only consideration is to take into account that a string like `eightwo`, is translated as `82`. Thus,
I have to maintain the first and last character of the spelled number.

```python
def map_spelled_numbers(s: str) -> str:
    s = s.replace('one', 'o1e')
    s = s.replace('two', 't2o')
    s = s.replace('three', 't3e')
    s = s.replace('four', 'f4r')
    s = s.replace('five', 'f5e')
    s = s.replace('six', 's6x')
    s = s.replace('seven', 's7n')
    s = s.replace('eight', 'e8t')
    s = s.replace('nine', 'n9e')
    return s.replace('zero', 'z0o')
```

The sum function is almost the same.

```python
def get_calibration_sum(lines: list[str]) -> int:
    return sum([map_lines_into_numbers(map_spelled_numbers(line)) for line in lines])
```

The answer is `54824`.

</details>

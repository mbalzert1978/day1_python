import pathlib
import typing


def reader(path: str | pathlib.Path) -> tuple[str, ...]:
    if isinstance(path, str):
        path = pathlib.Path(path)
    with pathlib.Path.open(path, "r") as f:
        return tuple(f)


def remove_alphas(data: typing.Iterable[str]) -> tuple[str, ...]:
    new_data = []
    for item in list(data):
        srg_ = "".join(letter for letter in item if letter.isdigit())
        new_data.append(srg_)
    return tuple(new_data)


def gather_valid(data: tuple[str, ...]) -> tuple[str, ...]:
    valid = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    new_data = []
    buffer = ""
    for item in data:
        srg = ""
        for letter in item:
            buffer += letter
            if buffer in valid:
                srg += valid[buffer]
                buffer = ""
                continue
            if letter.isdigit():
                srg += letter
                buffer = ""
        new_data.append(srg)
        buffer = ""
    return tuple(new_data)


def solver(data: typing.Iterable[str], filter_fn: typing.Callable) -> int:
    numbers = filter_fn(data)
    return sum(int(number[0] + number[-1]) for number in numbers)


pdata = (
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
)


def main():
    # Day 1 first half
    puzzle_data = reader("input.txt")
    result = solver(puzzle_data, remove_alphas)
    # Day 1 second half
    puzzle_data = pdata
    result = solver(puzzle_data, gather_valid)
    print(result)


if __name__ == "__main__":
    main()

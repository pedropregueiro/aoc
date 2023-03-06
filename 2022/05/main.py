import re
from collections import deque
from typing import Any, List, Tuple, Union


def batch_list(list_: Union[List, str], group_size: int):
    total_length = len(list_)
    for ndx in range(0, total_length, group_size):
        yield list_[ndx : min(ndx + group_size, total_length)]


def _print_stacks(stacks: List[Any]):
    for i, stack in enumerate(stacks, start=1):
        print(f"{i} | {stack}")


def parse_file_into_stacks_instructions(file_lines: List[str]) -> Tuple[List[Any], List[str]]:
    # todo (one day): all of this code could be improved and simplified
    instructions = []
    reversed_stacks = []
    for index, line in enumerate(file_lines):
        if line == "":
            continue
        elif line.startswith("move"):
            instructions.append(line)
        else:
            line_items = []
            for char in batch_list(line, group_size=4):
                clean_char = char.strip().replace("[", "").replace("]", "")
                line_items.append(clean_char)

            reversed_stacks.append(line_items)

    indices = reversed_stacks.pop(-1)
    max_len = int(indices[-1])

    # in order to zip all lists properly, they need to be the same length
    for rstack in reversed_stacks:
        if len(rstack) < max_len:
            rstack += [""] * (max_len - len(rstack))

    stacks = [list(z) for z in zip(*reversed_stacks)]

    # converting to string and stripping is just a quick way to remove the empty elems on top
    # deques are useful for inserting elems at both ends
    stacks = [deque("".join(s).strip()) for s in stacks]

    return stacks, instructions


def move_crates(stacks: List[deque], instr_line):
    qty_str, from_str, to_str = re.findall(r"move (\d+) from (\d+) to (\d+)", instr_line)[0]
    qty = int(qty_str)
    from_ = int(from_str) - 1
    to_ = int(to_str) - 1
    for _ in range(qty):
        elem = stacks[from_].popleft()
        stacks[to_].appendleft(elem)

    return stacks


def move_crates_9001(stacks: List[deque], instr_line):
    qty_str, from_str, to_str = re.findall(r"move (\d+) from (\d+) to (\d+)", instr_line)[0]
    qty = int(qty_str)
    from_ = int(from_str) - 1
    to_ = int(to_str) - 1

    new_elems = []
    for _ in range(qty):
        new_elems.append(stacks[from_].popleft())

    stacks[to_].extendleft(reversed(new_elems))

    return stacks


def get_top_crates(filename: str) -> str:
    with open(filename) as f:
        lines = f.read().splitlines()

    stacks, instructions = parse_file_into_stacks_instructions(file_lines=lines)
    print("Initial stacks:")
    _print_stacks(stacks)

    for instruction in instructions:
        print(f"\n# {instruction}")
        stacks = move_crates_9001(stacks, instruction)
        _print_stacks(stacks)

    top_crates = "".join([d[0] for d in stacks])

    print(f"\n# The crates on top of each stack are: {top_crates}")
    return top_crates


if __name__ == "__main__":
    assert get_top_crates("test_input.txt") == "MCD"
    get_top_crates("input.txt")

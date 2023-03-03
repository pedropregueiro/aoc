from string import ascii_letters
from typing import List, Set


def batch_list(list_: List, group_size: int):
    total_length = len(list_)
    for ndx in range(0, total_length, group_size):
        yield list_[ndx : min(ndx + group_size, total_length)]


def find_repeated_elements(comp1: str, comp2: str) -> Set[str]:
    repeated_elems = list(map(lambda elem: elem in comp2, comp1))
    return {comp1[index] for index, elem in enumerate(repeated_elems) if elem is True}


def find_group_repeated_element(group: List[str]) -> str:
    # this could probably be done in a smarter way
    repeated = set(group[0])
    for rem_rucksack in group[1:]:
        repeated = find_repeated_elements(str(repeated), rem_rucksack)

    if len(repeated) != 1:
        raise Exception("expected only 1 repeated element")

    return list(repeated)[0]


def calc_sum_priorities(filename) -> int:
    with open(filename) as f:
        lines = f.read().splitlines()

    sum_priorities = 0

    for group_lines in batch_list(lines, group_size=3):
        repeated = find_group_repeated_element(group_lines)
        alphabet_index = ascii_letters.index(repeated) + 1
        print(f"{group_lines} | repeated item: {repeated} | {alphabet_index}")

        sum_priorities += alphabet_index

    print(f"Sum of the priorities: {sum_priorities}")
    return sum_priorities


if __name__ == "__main__":
    assert calc_sum_priorities("test_input.txt") == 70
    calc_sum_priorities("input.txt")

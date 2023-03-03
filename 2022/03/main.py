from string import ascii_letters


def find_repeated_element(comp1: str, comp2: str) -> str:
    repeated_elems = list(map(lambda elem: elem in comp2, comp1))
    return comp1[repeated_elems.index(True)]


def calc_sum_priorities(filename) -> int:
    with open(filename) as f:
        lines = f.readlines()

    sum_priorities = 0

    for line in lines:
        line = line.strip()
        split_index = int(len(line) / 2)
        comp1, comp2 = line[:split_index], line[-split_index:]

        repeated = find_repeated_element(comp1, comp2)
        alphabet_index = ascii_letters.index(repeated) + 1
        print(f"{comp1} | {comp2} | repeated item: {repeated} | {alphabet_index}")

        sum_priorities += alphabet_index

    print(f"Sum of the priorities: {sum_priorities}")
    return sum_priorities


if __name__ == "__main__":
    assert calc_sum_priorities("test_input.txt") == 157
    calc_sum_priorities("input.txt")

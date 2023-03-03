def str_to_range(range_str: str) -> range:
    start, stop = range_str.split("-")
    return range(int(start), int(stop))


def is_fully_contained(range1: range, range2: range) -> bool:
    first_in_second = range1.start <= range2.start and range1.stop >= range2.stop
    second_in_first = range2.start <= range1.start and range2.stop >= range1.stop
    return first_in_second or second_in_first


def calc_fully_contained_pairs(filename) -> int:
    with open(filename) as f:
        lines = f.read().splitlines()

    fully_contained = 0
    for line in lines:
        first, second = line.split(",")
        first_pair = str_to_range(first)
        second_pair = str_to_range(second)
        is_contained = is_fully_contained(first_pair, second_pair)
        print(f"{first_pair} | {second_pair} | contained? {is_contained}")
        if is_contained:
            fully_contained += 1

    print(f"Number of assignments fully contained in their pair: {fully_contained}")
    return fully_contained


if __name__ == "__main__":
    assert calc_fully_contained_pairs("test_input.txt") == 2
    calc_fully_contained_pairs("input.txt")

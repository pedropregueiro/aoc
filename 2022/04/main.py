def str_to_range(range_str: str, inclusive: bool = False) -> range:
    start, stop = range_str.split("-")
    # Need to add an extra element because python range elements are: [start, stop[, instead of [start, stop]
    stop_int = int(stop) if not inclusive else int(stop) + 1
    return range(int(start), stop_int)


def is_fully_contained(range1: range, range2: range) -> bool:
    first_in_second = range1.start <= range2.start and range1.stop >= range2.stop
    second_in_first = range2.start <= range1.start and range2.stop >= range1.stop
    return first_in_second or second_in_first


def get_ranges_overlap(range1: range, range2: range) -> set:
    return set(range1) & set(range2)


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


def calc_overlapped_pairs(filename) -> int:
    with open(filename) as f:
        lines = f.read().splitlines()

    overlapped = 0
    for line in lines:
        first, second = line.split(",")
        first_pair = str_to_range(first, inclusive=True)
        second_pair = str_to_range(second, inclusive=True)
        overlap = get_ranges_overlap(first_pair, second_pair)
        print(f"{first_pair} | {second_pair} | overlap? {list(overlap)}")
        if len(overlap) > 0:
            overlapped += 1

    print(f"Number of assignments with an overlap: {overlapped}")
    return overlapped


if __name__ == "__main__":
    assert calc_overlapped_pairs("test_input.txt") == 4
    calc_overlapped_pairs("input.txt")

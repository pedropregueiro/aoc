def get_start_of_general(signal: str, distinct_count: int) -> int:
    buff_chars = []
    for marker, char in enumerate(signal, start=1):
        buff_chars.append(char)
        last4 = buff_chars[-distinct_count:]
        if len(set(last4)) == distinct_count:
            return marker


def get_start_of_packet_from_file(filename: str):
    with open(filename) as f:
        signal = f.read().strip()

    start_of_packet = get_start_of_general(signal, distinct_count=4)
    print(f"Start of packet is {start_of_packet}")


def get_start_of_message_from_file(filename: str):
    with open(filename) as f:
        signal = f.read().strip()

    start_of_message = get_start_of_general(signal, distinct_count=14)
    print(f"Start of message is {start_of_message}")


if __name__ == "__main__":
    # part 1
    assert get_start_of_general("mjqjpqmgbljsphdztnvjfqwrcgsmlb", distinct_count=4) == 7
    assert get_start_of_general("bvwbjplbgvbhsrlpgdmjqwftvncz", distinct_count=4) == 5
    assert get_start_of_general("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", distinct_count=4) == 10
    assert get_start_of_general("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", distinct_count=4) == 11
    get_start_of_packet_from_file("input.txt")

    # part 2
    assert get_start_of_general("mjqjpqmgbljsphdztnvjfqwrcgsmlb", distinct_count=14) == 19
    assert get_start_of_general("bvwbjplbgvbhsrlpgdmjqwftvncz", distinct_count=14) == 23
    assert get_start_of_general("nppdvjthqldpwncqszvftbrmjlhg", distinct_count=14) == 23
    assert get_start_of_general("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", distinct_count=14) == 29
    assert get_start_of_general("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", distinct_count=14) == 26
    get_start_of_message_from_file("input.txt")

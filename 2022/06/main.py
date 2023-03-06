def get_start_of_packet(signal: str) -> int:
    buff_chars = []
    for marker, char in enumerate(signal, start=1):
        buff_chars.append(char)
        last4 = buff_chars[-4:]
        if len(set(last4)) == 4:
            return marker


def get_start_of_packet_from_file(filename: str):
    with open(filename) as f:
        signal = f.read().strip()

    start_of_packet = get_start_of_packet(signal)
    print(f"Start of packet is {start_of_packet}")


if __name__ == "__main__":
    assert get_start_of_packet("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert get_start_of_packet("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert get_start_of_packet("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert get_start_of_packet("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11
    get_start_of_packet_from_file("input.txt")

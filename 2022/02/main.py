from enum import Enum


class Moves(Enum):
    # tuple enum with string representation, shape value and winning opponent
    Rock = ("Rock", 1, "Paper")
    Paper = ("Paper", 2, "Scissors")
    Scissors = ("Scissors", 3, "Rock")

    def __str__(self):
        return self.value[0]

    def __gt__(self, other):
        if self.value[2] == other.value[0]:
            return False
        else:
            return True

    def versus(self, other) -> int:
        if self == other:
            return 3
        elif self > other:
            return 6
        else:
            return 0


# this feels wrong...
possible_moves = {
    "A": Moves.Rock,
    "B": Moves.Paper,
    "C": Moves.Scissors,
    "X": Moves.Rock,
    "Y": Moves.Paper,
    "Z": Moves.Scissors,
}


def calc_score(input_filename: str) -> int:
    with open(input_filename) as f:
        lines = f.readlines()

    total_score = 0

    for line in lines:
        opp_move_str, should_move_str = line.strip().split(" ")

        opp_move = possible_moves[opp_move_str]
        should_move = possible_moves[should_move_str]

        shape_score = should_move.value[1]
        versus_score = should_move.versus(opp_move)
        round_score = shape_score + versus_score

        print(f"opponent played {opp_move} | should play: {should_move} | score: {round_score}")

        total_score += round_score

    return total_score


if __name__ == "__main__":
    assert calc_score("test_input.txt") == 15
    score = calc_score("input.txt")
    print(f"Total score: {score}")

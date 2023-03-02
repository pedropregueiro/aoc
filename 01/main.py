if __name__ == "__main__":
    elves = []

    with open("input.txt") as f:
        lines = f.readlines()

    curr_elf_calories_intake = 0
    for line in lines:
        if line == "\n":
            elves.append(curr_elf_calories_intake)
            curr_elf_calories_intake = 0
        else:
            curr_elf_calories_intake += int(line)

    elves.append(curr_elf_calories_intake)
    curr_elf_calories_intake = 0

    sorted_elves = sorted(elves, reverse=True)
    elf_index = elves.index(sorted_elves[0]) + 1

    print(f"[part 1] The heaviest elf is {elf_index} with {sorted_elves[0]} calories")
    print(f"[part 2] The 3 heaviest elves are carrying {sum(sorted_elves[:3])} calories")

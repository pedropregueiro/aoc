if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    curr_elf_index = 1
    curr_elf_calories_intake = 0

    heaviest_elf_index = -1
    heaviest_elf_intake = -1

    for line in lines:
        if line == "\n":
            if curr_elf_calories_intake > heaviest_elf_intake:
                heaviest_elf_intake = curr_elf_calories_intake
                heaviest_elf_index = curr_elf_index

            curr_elf_index += 1
            curr_elf_calories_intake = 0
        else:
            curr_elf_calories_intake += int(line)

    print(f"The heaviest elf is {heaviest_elf_index} with {heaviest_elf_intake} calories")

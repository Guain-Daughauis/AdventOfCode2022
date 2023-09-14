# Read the input file into a list of elves
with open("in.txt", "r", encoding="utf8") as f:
    elves = f.read().split("\n\n")

# Calculate the total calories for each elf and sort them in descending order
elf_calories = [sum(map(int, elf.splitlines())) for elf in elves]
elf_calories.sort(reverse=True)

# Calculate the sum of the top three fattest elves
total_calories = sum(elf_calories[:3])

print(total_calories)
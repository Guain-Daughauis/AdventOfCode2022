# Read the input file into a list of elves
with open("in.txt", "r", encoding="utf8") as f:
    elves = f.read().split("\n\n")

# Initialize variables
max_calories = 0
fat_elf = 0

# Iterate through the elves
for index, elf in enumerate(elves, start=1):
    print(f"Checking Elf Nº {index}'s bag")
    calories = [int(calory) for calory in elf.splitlines()]
    total_calories = sum(calories)
    print(f"In total, Elf Nº {index} is carrying {total_calories} calories")
    
    if total_calories > max_calories:
        print(f"Elf Nº {index} was carrying more than {max_calories} calories and now is the fattest elf.")
        max_calories = total_calories
        fat_elf = index

print(f"The fattest elf is Elf Nº {fat_elf}, he's carrying {max_calories} calories")
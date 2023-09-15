# Copyright (C) 2023 Guain-Daughauis <guain_daughauis@protonmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

# Define a dictionary to map characters to their priorities
priority_mapping: dict[str, int] = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,'t': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

with open(file="in.txt", mode="r", encoding="utf8") as f:
    rucksacks: list[str] = f.read().splitlines()

total_shared = 0

# Use range to iterate through rucksacks in groups of 3
for i in range(0, len(rucksacks), 3):
    group: list[str] = rucksacks[i:i+3]
    
    # Calculate shared characters using set intersection
    shared: set[str] = set(group[0]) & set(group[1]) & set(group[2])
    
    if shared:
        shared_char: str = shared.pop()
        shared_priority: int = priority_mapping.get(shared_char, -999)
        total_shared += shared_priority
        print(f"({shared_priority}) {shared_char}")

print(f"Total is {total_shared}")
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

# Use the dictionary to get the priority value

with open(file="in.txt", mode="r", encoding="utf8") as f:
    lines: list[str] = [line.strip() for line in f]

overlaps = 0

for line in lines:
    elf_a, elf_b = line.split(',')
    elf_a_min, elf_a_max = map(int, elf_a.split('-'))
    elf_b_min, elf_b_max = map(int, elf_b.split('-'))
    
    if (elf_a_min <= elf_b_min <= elf_b_max <= elf_a_max) or (elf_b_min <= elf_a_min <= elf_a_max <= elf_b_max):
        overlaps += 1

print(overlaps)
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

def rock_paper_scissor(opponent: str, you: str) -> int:
    scores: dict[str, int] = {'AX': 3, 'AY': 6, 'AZ': 0, 'BX': 0, 'BY': 3, 'BZ': 6, 'CX': 6, 'CY': 0, 'CZ': 3}
    return scores.get(opponent + you, 0) + {'X': 1, 'Y': 2, 'Z': 3}.get(you, 0)

with open(file="in.txt", mode="r", encoding="utf8") as f:
    rounds: list[str] = [line.strip() for line in f]

total_score: int = sum(rock_paper_scissor(*round.split()) for round in rounds)
print(total_score)

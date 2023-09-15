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
    score_mapping: dict[str, int] = {
        'AX': 3, 'AY': 4, 'AZ': 5,
        'BX': 1, 'BY': 5, 'BZ': 9,
        'CX': 2, 'CY': 6, 'CZ': 7,
    }
    return score_mapping.get(opponent + you, -99999999)

with open(file="in.txt", mode="r", encoding="utf8") as f:
    rounds: list[str] = [line.strip() for line in f]

total_score: int = sum(rock_paper_scissor(*round.split()) for round in rounds)
print(total_score)

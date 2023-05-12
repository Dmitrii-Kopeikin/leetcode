from typing import List
from copy import deepcopy


class Solution:

    def gameOfLife(self, board: List[List[int]]) -> None:
        input_board = deepcopy(board)
        for n in range(len(board[0])):
            for m in range(len(board)):
                # checking cell
                alive_neighboors = 0
                for x in range(n - 1, n + 2):
                    if  not (-1 < x < len(board[0])):
                        continue
                    for y in range(m - 1, m + 2):
                        if not (-1 < y < len(board) and (y != m or x != n)):
                            continue
                        alive_neighboors += input_board[y][x]

                if (board[m][n] == 1 and alive_neighboors in [2, 3]
                        or board[m][n] == 0 and alive_neighboors == 3):
                    board[m][n] = 1
                else:
                    board[m][n] = 0

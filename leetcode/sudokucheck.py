# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
#     Each row must contain the digits 1-9 without repetition.
#     Each column must contain the digits 1-9 without repetition.
#     Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Example 1:
#
# Input:
# [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: true
#
# Example 2:
#
# Input:
# [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        rowsSeen = [[] for _ in range(9)]
        colsSeen = [[] for _ in range(9)]

        # iterate 3x3
        # for each item, figure out which row/col/square to add it to

        for x in range(3):
            for y in range(3):
                square = []
                for x_ in range(3):
                    for y_ in range(3):
                        c = board[x*3 + x_][y*3 + y_]
                        if not c == ".":
                            if c in square:
                                return False
                            square.append(c)

                            if c in rowsSeen[y*3 + y_]:
                                return False
                            rowsSeen[y*3 + y_].append(c)

                            if c in colsSeen[x*3 + x_]:
                                return False
                            colsSeen[x*3 + x_].append(c)
        return True

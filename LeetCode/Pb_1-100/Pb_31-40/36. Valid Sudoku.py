""" Determine if a 9 x 9 Sudoku board is valid.
Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
without repetition.

Note:

. A Sudoku board (partially filled) could be valid but
is not necessarily solvable.
. Only the filled cells need to be validated according to the mentioned rules.

Example 1:

Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false

Explanation: Same as Example 1,
except with the 5 in the top left corner being modified to 8.
Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'. """


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        count_val = 0
        count_set = 0

        # check line
        for i in range(9):
            set_board = set()
            for j in range(9):
                if board[i][j] != ".":
                    set_board.add(board[i][j])
                    count_val += 1

            count_set = len(set_board)
            if count_val != count_set:
                return False
            count_val = 0

        # check column
        for i in range(9):
            set_board = set()
            for j in range(9):
                if board[j][i] != ".":
                    set_board.add(board[j][i])
                    count_val += 1

            count_set = len(set_board)
            if count_val != count_set:
                return False
            count_val = 0

        # check block
        k = 0
        m = 0
        while k < 9:
            set_board = set()
            if m <= 6:
                for i in range(k, k + 3):

                    for j in range(m, m + 3):
                        if board[i][j] != ".":
                            set_board.add(board[i][j])
                            count_val += 1

                count_set = len(set_board)
                if count_val != count_set:
                    return False
                count_val = 0

                m += 3
            else:
                k += 3
                m = 0

        return True

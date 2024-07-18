def main():
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

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
            print("False1")
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
            print("False2")
            return False
        count_val = 0

    # check block
    k = 0
    l = 0
    while k < 9:
        set_board = set()
        if l <= 6:
            for i in range(k, k + 3):

                for j in range(l, l + 3):
                    if board[i][j] != ".":
                        set_board.add(board[i][j])
                        count_val += 1

            count_set = len(set_board)
            if count_val != count_set:
                print("False3")
                return False
            count_val = 0

            l += 3
        else:
            k += 3
            l = 0

    print("True")
    return True


main()

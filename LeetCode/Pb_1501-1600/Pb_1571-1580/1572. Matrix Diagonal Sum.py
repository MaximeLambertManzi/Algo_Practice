class Solution:
    def diagonalSum(self, mat) -> int:

        sum_total = 0
        size = len(mat)

        for i in range(size):
            sum_total += mat[i][i]
            sum_total += mat[i][size - i - 1]

        if size % 2 == 1:
            mid = size // 2
            sum_total -= mat[mid][mid]

        return sum_total

class Solution:
    def generate(self, numRows: int):

        pascal = [[1]]
        row = []

        if numRows == 1:
            return pascal

        for i in range(1, numRows):

            row.append(1)
            for j in range(len(pascal[i - 1]) - 1):
                row.append(pascal[i - 1][j] + pascal[i - 1][j + 1])
            row.append(1)
            pascal.append(row)

            row = []

        return pascal

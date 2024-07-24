""" In MATLAB, there is a handy function called reshape which can reshape
an m x n matrix into a new one with a different size r x c
keeping its original data.

You are given an m x n matrix mat and two integers r and c
representing the number of rows and the number of columns
of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements
of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal,
output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:

Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:

Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
-1000 <= mat[i][j] <= 1000
1 <= r, c <= 300 """


class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        mat_1d = list()
        row = len(mat)
        column = len(mat[0])

        if row * column == r * c:
            for i in range(row):
                mat_1d.extend(mat[i])

            mat_final = list()
            line_temp = list()
            k = 0
            for i in range(r):

                for j in range(c):
                    line_temp.append(mat_1d[k])
                    k += 1

                mat_final.append(line_temp)
                line_temp = []

            return mat_final
        else:
            return mat

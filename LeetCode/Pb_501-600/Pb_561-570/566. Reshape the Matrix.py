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

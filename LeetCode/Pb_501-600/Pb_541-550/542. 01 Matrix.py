class Solution:
    def updateMatrix(self, mat):
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        len_x = len(mat)
        len_y = len(mat[0])

        queue = list()
        res = [[-1 for _ in range(len_y)] for _ in range(len_x)]

        for i in range(len_x):
            for j in range(len_y):

                if mat[i][j] == 0:
                    res[i][j] = 0
                    queue.append((i, j))

        while queue:

            cur_i, cur_j = queue.pop(0)
            for x, y in dir:
                next_i, next_j = cur_i + x, cur_j + y
                if (
                    0 <= next_i < len_x
                    and 0 <= next_j < len_y
                    and res[next_i][next_j] == -1
                ):
                    res[next_i][next_j] = res[cur_i][cur_j] + 1
                    queue.append((next_i, next_j))

        return res

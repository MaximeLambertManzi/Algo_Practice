from copy import deepcopy


class Solution:
    def checkNoFresh(self, grid, len_x, len_y):
        for i in range(len_x):
            for j in range(len_y):
                if grid[i][j] == 1:
                    return False

        return True

    def checkNext(self, grid, x, y, len_x, len_y):
        dir_vect = ((-1, 0), (1, 0), (0, 1), (0, -1))

        for i, j in dir_vect:
            cur_x = x + i
            cur_y = y + j

            if 0 <= cur_x < len_x and 0 <= cur_y < len_y and grid[cur_x][cur_y] == 2:
                return 2

        return 1

    def orangesRotting(self, grid) -> int:

        days = 0
        len_x = len(grid)
        len_y = len(grid[0])

        rotten = self.checkNoFresh(grid, len_x, len_y)
        if rotten:
            return 0

        while not rotten:
            temp_grid = [[-1 for _ in range(len_y)] for _ in range(len_x)]

            for i in range(len_x):
                for j in range(len_y):
                    if grid[i][j] == 1:
                        temp_grid[i][j] = self.checkNext(grid, i, j, len_x, len_y)
                    else:
                        temp_grid[i][j] = grid[i][j]

            if grid == temp_grid:
                return -1

            days += 1
            rotten = self.checkNoFresh(temp_grid, len_x, len_y)
            grid = deepcopy(temp_grid)

        return days

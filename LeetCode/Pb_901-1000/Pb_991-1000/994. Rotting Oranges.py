""" You are given an m x n grid where each cell can have one of three values:

. 0 representing an empty cell,
. 1 representing a fresh orange, or
. 2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally
adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse
until no cell has a fresh orange. If this is impossible, return -1.

Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1

Explanation: The orange in the bottom left corner (row 2, column 0)
is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: grid = [[0,2]]
Output: 0

Explanation: Since there are already no fresh oranges at minute 0,
the answer is just 0.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2. """

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

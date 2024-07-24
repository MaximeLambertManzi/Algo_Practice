""" You are given an m x n binary matrix grid.
An island is a group of 1's (representing land)
connected 4-directionally (horizontal or vertical).
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6

Explanation: The answer is not 11,
because the island must be connected 4-directionally.

Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1. """


class Solution:
    def search_size(self, grid, x, y, len_x, len_y, size, visited):
        if (x, y) not in visited:
            visited.add((x, y))
            if grid[x][y] == 1:

                size += 1

                if x > 0:
                    size = self.search_size(grid, x - 1, y, len_x, len_y, size, visited)
                if x < len_x - 1:
                    size = self.search_size(grid, x + 1, y, len_x, len_y, size, visited)
                if y > 0:
                    size = self.search_size(grid, x, y - 1, len_x, len_y, size, visited)
                if y < len_y - 1:
                    size = self.search_size(grid, x, y + 1, len_x, len_y, size, visited)

        return size

    def maxAreaOfIsland(self, grid) -> int:
        len_x = len(grid)
        len_y = len(grid[0])

        list_size_islands = [0]

        visited = set()

        for i in range(len_x):
            for j in range(len_y):

                res = self.search_size(grid, i, j, len_x, len_y, 0, visited)
                if res != 0:
                    list_size_islands.append(res)
        return max(list_size_islands)

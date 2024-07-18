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

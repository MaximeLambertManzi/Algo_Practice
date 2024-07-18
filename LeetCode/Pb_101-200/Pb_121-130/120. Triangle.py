class Solution:
    def minimumTotal(self, triangle) -> int:
        height = len(triangle)
        min_path = [[[0] for i in range(len(row))] for row in triangle]
        min_path[0][0] = triangle[0][0]

        if height == 1:
            return min_path[0][0]
        else:
            for i in range(1, height):
                for j in range(len(triangle[i])):
                    if j == 0:
                        min_path[i][j] = min_path[i - 1][j] + triangle[i][j]
                    elif j == len(triangle[i]) - 1:
                        min_path[i][j] = min_path[i - 1][j - 1] + triangle[i][j]
                    else:
                        min_path[i][j] = (
                            min(min_path[i - 1][j], min_path[i - 1][j - 1])
                            + triangle[i][j]
                        )

        return min(min_path[-1])

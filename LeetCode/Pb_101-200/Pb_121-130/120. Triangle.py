""" Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below.
More formally, if you are on index i on the current row,
you may move to either index i or index i + 1 on the next row.

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11

Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:

Input: triangle = [[-10]]
Output: -10

Constraints:

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104

Follow up: Could you do this using only O(n) extra space,
where n is the total number of rows in the triangle?
 """


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

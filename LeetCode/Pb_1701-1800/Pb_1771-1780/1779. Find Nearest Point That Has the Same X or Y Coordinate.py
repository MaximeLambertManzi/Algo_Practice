class Solution:
    def nearestValidPoint(self, x: int, y: int, points) -> int:

        curr_loc = [x, y]

        def manhattan_dist(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

        man_point = 0
        min_man = 100000
        min_index = 10001

        for point in points:
            if point[0] == x or point[1] == y:
                man_point = manhattan_dist(curr_loc, point)
                if man_point < min_man:
                    min_man = man_point
                    min_index = points.index(point)

        if min_index != 10001:
            return min_index
        else:
            return -1

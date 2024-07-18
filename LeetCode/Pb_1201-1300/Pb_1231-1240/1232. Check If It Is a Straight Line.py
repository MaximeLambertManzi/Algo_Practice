class Solution:
    def checkStraightLine(self, coordinates) -> bool:

        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        for x, y in coordinates:
            if (x - x0) * (y1 - y0) != (y - y0) * (x1 - x0):
                return False
        else:
            return True

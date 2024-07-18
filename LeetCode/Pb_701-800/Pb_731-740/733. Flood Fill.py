class Solution:
    def fourDirFlood(self, image, x1, y1, value, len_x, len_y, origin_color):

        image[x1][y1] = value

        x2 = x1 - 1
        y2 = y1
        if x2 >= 0:
            if image[x2][y2] == origin_color:
                self.fourDirFlood(image, x2, y2, value, len_x, len_y, origin_color)

        x2 = x1 + 1
        y2 = y1
        if x2 < len_x:
            if image[x2][y2] == origin_color:
                self.fourDirFlood(image, x2, y2, value, len_x, len_y, origin_color)

        x2 = x1
        y2 = y1 - 1
        if y2 >= 0:
            if image[x2][y2] == origin_color:
                self.fourDirFlood(image, x2, y2, value, len_x, len_y, origin_color)

        x2 = x1
        y2 = y1 + 1
        if y2 < len_y:
            if image[x2][y2] == origin_color:
                self.fourDirFlood(image, x2, y2, value, len_x, len_y, origin_color)

    def floodFill(self, image, sr: int, sc: int, color: int):
        len_x = len(image)
        len_y = len(image[0])
        origin_color = image[sr][sc]

        if color == origin_color:
            return image
        else:
            self.fourDirFlood(image, sr, sc, color, len_x, len_y, origin_color)
            return image

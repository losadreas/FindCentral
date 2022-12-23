
from functools import lru_cache
class Image:
    def __init__(self, data, w, h):
        self.pixels = data
        self.width = w
        self.height = h


class Central_Pixels_Finder(Image):
    def __init__(self):
        self.make_x_y_dict()
        self.make_info_by_position()
        self.adding_quantity()
        self.dict_colors = self.make_dict_colors()
        self.dict_points = self.find_central()

    def central_pixels(self, colour):
        if colour in self.dict_points:
            return self.dict_points[colour]
        else:
            return []

    def make_x_y_dict(self):
        image = self.pixels.copy()
        self.dict_image = {}
        for line in range(self.height):
            self.dict_image[line] = {}
            for row in range(self.width):
                self.dict_image[line][row] = [image.pop(0)]

    def make_info_by_position(self):
        row_max = self.width
        line_max = self.height
        for line, row in self.dict_image.items():
            for r in row:
                if line == 0 or line == line_max - 1 or r == 0 or r == row_max - 1:
                    self.dict_image[line][r].append(0)
                else:
                    color_cur = self.dict_image[line][r][0]
                    if self.dict_image[line - 1][r][0] == color_cur and \
                            self.dict_image[line + 1][r][0] == color_cur and \
                            self.dict_image[line][r - 1][0] == color_cur and \
                            self.dict_image[line][r + 1][0] == color_cur:
                        self.dict_image[line][r].append(1)
                    else:
                        self.dict_image[line][r].append(0)

    def adding_quantity(self):
        for line, row in self.dict_image.items():
            for r in row:
                max_quantity = 1
                if self.dict_image[line][r][1] == 0:
                    self.dict_image[line][r].append(0)
                else:
                    for i in range(1, self.height):
                        result = self.dict_image[line + i][r][1] + self.dict_image[line - i][r][1] + \
                                 self.dict_image[line][r - i][1] + self.dict_image[line][r + i][1]
                        if result < 4:
                            break
                        else:
                            max_quantity += 1
                    self.dict_image[line][r].append(max_quantity)

    def make_dict_colors(self):
        dict_colors = {}
        for line, row in self.dict_image.items():
            for r in row:
                color = self.dict_image[line][r][0]
                quantity = self.dict_image[line][r][2]
                if color in dict_colors:
                    dict_colors[color].add(quantity)
                else:
                    dict_colors[color] = {quantity}
        for color in dict_colors:
            dict_colors[color] = max(dict_colors[color])
        return dict_colors

    def find_central(self):
        dict_points = {}
        row_max = self.width
        for line, row in self.dict_image.items():
            for r in row:
                color = self.dict_image[line][r][0]
                if self.dict_image[line][r][2] == self.dict_colors[color]:
                    if color in dict_points:
                        dict_points[color].append(line * row_max + r)
                    else:
                        dict_points[color] = [line * row_max + r]
        return dict_points

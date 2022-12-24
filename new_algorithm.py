class Central_Pixels_Finder:
    def __init__(self, data, w, h):
        self.pixels = data
        self.width = w
        self.height = h
        self.dict_colour = {}
        self.create_dict_image()
        self.create_outside_set()
        self.main_algorithm()

    def central_pixels(self, colour):
        self.create_dict_image()
        self.create_outside_set()
        self.main_algorithm()
        # self.make_x_y_dict()
        # self.make_info_by_position()
        # self.adding_quantity()
        # self.make_dict_colors()
        # self.find_central()
        if colour in self.dict_points:
            return self.dict_points[colour]
        else:
            return []

    def create_dict_image(self):
        self.dict_image = {}
        counter = 0
        for colour in self.pixels:
            if colour in self.dict_image:
                self.dict_image[colour].add(counter)
            else:
                self.dict_image[colour] = {counter}
            counter += 1

    def create_outside_set(self):
        self.set_outside = set()
        for i in range(self.width):
            self.set_outside.add(i)
        for i in range(self.width * (self.height - 1), self.width * self.height):
            self.set_outside.add(i)
        for i in range(self.width, self.width * self.height, self.width):
            self.set_outside.add(i)
            self.set_outside.add(i + self.width - 1)

    def main_algorithm(self):
        for colour in self.dict_image:
            print(colour, self.dict_image[colour])
            # self.set_quantity(colour)

    def set_quantity(self, colour):
        self.dict_colour[colour] = {}
        # for pixel in self.dict_image[colour]:
        #     for i in range(self.width):
        #
        #     print(pixel)

    def check_with_outside(self, pixel):
        return pixel in self.set_outside

    def check_with_presence_in_colour_set(self, pixel, colour):
        return pixel in self.dict_image[colour]

    def create_four_neighbor_pixel(self, pixel):
        pixel_left = pixel - 1
        pixel_right = pixel + 1
        pixel_up = pixel - self.width
        pixel_down = pixel + self.width
        return [pixel_left, pixel_right, pixel_up, pixel_down]


image = Central_Pixels_Finder([1, 1, 4, 4, 4, 4, 2, 2, 2, 2,
                               1, 1, 1, 1, 2, 2, 2, 2, 2, 2,
                               1, 1, 1, 1, 2, 2, 2, 2, 2, 2,
                               1, 1, 1, 1, 1, 3, 2, 2, 2, 2,
                               1, 1, 1, 1, 1, 3, 3, 3, 2, 2,
                               1, 1, 1, 1, 1, 1, 3, 3, 3, 3], 10, 6)

print(image.check_with_outside(12))
image.set_quantity(4)
print(image.check_with_presence_in_colour_set(3, 1))
print(image.create_four_neighbor_pixel(20))

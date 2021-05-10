token = '🔳'

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.g = [
            [
                None for _ in range(self.width)
            ] for _ in range(self.height)
        ]

    def write(self, position, val):
        x, y = position
        self.g[-y][x] = val

    def get(self):
        return self.g

    def render(self):
        # account for 2 vertical borders either side
        horizontal_border = token * (self.width + 2) + '\n'
        out = horizontal_border
        for row in self.g:
            combined_row = token
            for val in row:
                combined_row += '  ' if val is None else val
            out += combined_row + token+ '\n'
        out += horizontal_border
        return out

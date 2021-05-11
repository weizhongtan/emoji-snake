token = '🔳'

class Grid:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._grid = [
            [
                None for _ in range(self._width)
            ] for _ in range(self._height)
        ]

    def write(self, position, val):
        x, y = position
        self._grid[-y][x] = val

    def get(self):
        return self._grid

    def render(self):
        # account for 2 vertical borders either side
        horizontal_border = token * (self._width + 2) + '\n'
        out = horizontal_border
        for row in self._grid:
            combined_row = token
            for val in row:
                combined_row += '  ' if val is None else val
            out += combined_row + token+ '\n'
        out += horizontal_border
        return out

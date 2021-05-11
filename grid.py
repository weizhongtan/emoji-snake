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
        out = []

        # account for 2 vertical borders either side
        horizontal_border = token * (self._width + 2)
        out.append(horizontal_border)

        for row in self._grid:
            combined_row = ''
            for val in row:
                combined_row += '  ' if val is None else val
            out.append(token + combined_row + token)

        out.append(horizontal_border)

        return out

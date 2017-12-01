# Globals for the bearings
# Change the values as you see fit
EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self._x = x
        self._y = y
        self._bearing = bearing

    @property
    def coordinates(self):
        return (self._x, self._y)

    @property
    def bearing(self):
        return self._bearing

    def turn_right(self):
        if self._bearing == EAST:
            self._bearing = SOUTH
        else:
            self._bearing -= 1

    def turn_left(self):
        if self._bearing == SOUTH:
            self._bearing = EAST
        else:
            self._bearing += 1

    def advance(self):
        if self._bearing == EAST:
            self._x += 1
        elif self._bearing == NORTH:
            self._y += 1
        elif self._bearing == WEST:
            self._x -= 1
        elif self._bearing == SOUTH:
            self._y -= 1

    def simulate(self, txt):
        for x in txt:
            if x == 'L':
                self.turn_left()
            elif x == 'R':
                self.turn_right()
            elif x == 'A':
                self.advance()

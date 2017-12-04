class Point(object):

    def __init__(self, val, x, y):
        self.value = val
        self.x = x
        self.y = y

class Grid(object):

    def __init__(self):
        self.last_move = None
        self.move_counter = 1
        self.current_sequence = []
        self.points = []

    def add_point(self, value):
        if len(self.points) == 0:
            self.points.append(Point(value, 0, 0))
        else:
            move = self._next()
            if move == 'L':
                next_x, next_y = self._left()
            elif move == 'D':
                next_x, next_y = self._down()
            elif move == 'R':
                next_x, next_y = self._right()
            else:
                next_x, next_y = self._up()
            self.last_move = move
            self.current_sequence.append(move)
            self.points.append(Point(value, next_x, next_y))

    def distance(self, value):
        find_point = [pt for pt in self.points if pt.value == value]
        if len(find_point) == 0:
            return None
        else:
            return abs(find_point[0].x) + abs(find_point[0].y)

    def _next(self):
        order = 'RULD'
        if self.last_move is None:
            return order[0]
        elif len(self.current_sequence) == self.move_counter:
            idx = order.index(self.last_move) + 1
            idx = 0 if idx == len(order) else idx
            if self.last_move in 'DU':
                self.move_counter += 1
            self.current_sequence.clear()
            return order[idx]
        else:
            return self.last_move

    def _right(self):
        return self.points[-1].x + 1, self.points[-1].y

    def _up(self):
        return self.points[-1].x, self.points[-1].y + 1

    def _left(self):
        return self.points[-1].x - 1, self.points[-1].y

    def _down(self):
        return self.points[-1].x, self.points[-1].y - 1

puzzle_input = 347991
grid = Grid()
for x in range(1, puzzle_input + 1):
    grid.add_point(x)

print('{} steps'.format(grid.distance(puzzle_input)))

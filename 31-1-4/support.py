import math


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def plus_x(self, x):
        return Point(self.x + x, self.y)

    def plus_y(self, y):
        return Point(self.x, self.y + y)

    def plus(self, value, direction):
        if direction == top:
            return self.plus_y(-value)
        if direction == right:
            return self.plus_x(value)
        if direction == bottom:
            return self.plus_y(value)
        if direction == left:
            return self.plus_x(-value)
        raise Exception('Unknown direction')

    def value_in_direction(self, direction):
        if direction == top:
            return -self.y
        if direction == right:
            return self.x
        if direction == bottom:
            return self.y
        if direction == left:
            return -self.x

    def distance(self, another):
        return abs(self.x - another.x) + abs(self.y - another.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __str__(self):
        return f'[{self.x}, {self.y}]'


class Steps:
    def __init__(self):
        self.steps = []

    def add_step(self, point_from, point_to):
        self.steps.append((point_from, point_to))

    def __str__(self):
        s = ''
        for step in self.steps:
            s += f'{step[0]} -> {step[1]}\n'
        return s


top, right, bottom, left = 0, 1, 2, 3


def combine_directions(base, second):
    return (base + second) % 4


def _sgn(x):
    if x < 0:
        return -1
    if x > 0:
        return 1
    return 0


def get_distance(steps_A, steps_B, width):
    distance = 0
    B_stop = None
    for step_A in steps_A.steps:
        if B_stop is not None:
            break
        for step_B in steps_B.steps:
            start_A, end_A = step_A
            start_B, end_B = step_B

            if end_A == end_B:
                if start_A.x == start_B.x and _sgn(end_A.y - start_A.y) == _sgn(end_B.y - start_B.y):
                    distance += abs(abs(end_A.y - start_A.y) - abs(end_B.y - start_B.y)) + 1
                    B_stop = start_B
                    break
                if start_A.y == start_B.y and _sgn(end_A.x - start_A.x) == _sgn(end_B.x - start_B.x):
                    distance += abs(abs(end_A.x - start_A.x) - abs(end_B.x - start_B.x)) + 1
                    B_stop = start_B
                    break
        if B_stop is None:
            distance += abs(end_A.x - start_A.x) + abs(end_A.y - start_A.y)
    print(distance)
    for step_B in steps_B.steps:
        start_B, end_B = step_B
        if B_stop is not None and start_B == B_stop:
            return distance
        distance += abs(end_B.x - start_B.x) + abs(end_B.y - start_B.y)

    end_A, end_B = steps_A.steps[len(steps_A.steps) - 1][1], steps_B.steps[len(steps_B.steps) - 1][1]
    if end_A.x == end_B.x == 0 or end_A.x == end_B.x == width + 1:
        distance += abs(end_A.y - end_B.y)
    elif end_A.y == end_B.y == 0 or end_A.y == end_B.y == width + 1:
        distance += abs(end_A.x - end_B.x)
    corners = [Point(0, 0), Point(0, width + 1), Point(width + 1, width + 1), Point(0, width + 1)]
    distance += min([end_A.distance(corner) + end_B.distance(corner) + 1 for corner in corners])
    return distance

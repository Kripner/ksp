from math import ceil

from support import *

s = "30 52075694 1351123829 1200311067 592452736"
parts = s.split(' ')
N = int(parts[0])
a = Point(int(parts[2]), int(parts[1]))
b = Point(int(parts[4]), int(parts[3]))

steps = Steps()


def extract_point(point, n, left_top, width, orientation, steps):
    assert n > 0
    if point.x < left_top.x or point.y < left_top.y or point.x >= left_top.x + width or point.y >= left_top.y + width:
        return point
    # relative_left_top = left_top
    # if orientation == left or orientation == bottom:
    #     relative_left_top = relative_left_top.plus_y(width - 1)
    # if orientation == right or orientation == bottom:
    #     relative_left_top = relative_left_top.plus_x(width - 1)
    half_width = width // 2
    middle_point = left_top.plus_y(half_width).plus_x(half_width)
    if n == 1:
        exit_point = middle_point.plus(1, orientation)
        if point != exit_point and point != middle_point:
            raise Exception('The point is in a wall!')
        extracted_point = exit_point.plus(1, orientation)
        steps.add_step(point, extracted_point)
        return extracted_point

    if point.x != left_top.x + half_width and point.y != left_top.y + half_width:
        sub_orientations = [combine_directions(orientation, left), combine_directions(orientation, right), orientation, orientation]
        point = extract_point(point, n - 1, left_top, half_width, sub_orientations[0 - orientation % 4], steps)
        point = extract_point(point, n - 1, left_top.plus_x(half_width + 1), half_width, sub_orientations[(1 - orientation) % 4], steps)
        point = extract_point(point, n - 1, left_top.plus_x(half_width + 1).plus_y(half_width + 1), half_width, sub_orientations[(2 - orientation) % 4], steps)
        point = extract_point(point, n - 1, left_top.plus_y(half_width + 1), half_width, sub_orientations[(3 - orientation) % 4], steps)

    if point.x < left_top.x or point.y < left_top.y or point.x >= left_top.x + width or point.y >= left_top.y + width:
        return point
    if point.x != left_top.x + half_width and point.y != left_top.y + half_width:
        raise Exception('Failed to extract the point!')

    relative_right = combine_directions(orientation, right)
    right_shift = point.value_in_direction(relative_right) - middle_point.value_in_direction(relative_right)
    if right_shift != 0:
        centered_point = point.plus(-right_shift, relative_right)
        assert middle_point == centered_point
        steps.add_step(point, centered_point)
        point = centered_point
    if point.value_in_direction(orientation) >= middle_point.value_in_direction(orientation):
        extracted_point = middle_point.plus(half_width + 1, orientation)
    else:
        extracted_point = middle_point.plus(half_width + 1, combine_directions(orientation, bottom))
    assert point != extracted_point
    steps.add_step(point, extracted_point)
    return extracted_point


steps_A, steps_B = Steps(), Steps()
width = (2 ** (N + 1)) - 1
print(extract_point(a, N, Point(1, 1), width, top, steps_A))
print(extract_point(b, N, Point(1, 1), width, top, steps_B))
print(steps_A)
print(steps_B)
result = get_distance(steps_A, steps_B, width)
print(result)

name = '07'
f = open(f'{name}.out', 'w')
f.write(str(result) + '\n')
f.close()

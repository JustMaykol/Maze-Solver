def get_near(value):
    return [get_up(value), get_right(value), get_down(value), get_left(value)]


def get_up(value):
    return [value[0], value[1] - 1]


def get_right(value):
    return [value[0] + 1, value[1]]


def get_down(value):
    return [value[0], value[1] + 1]


def get_left(value):
    return [value[0] - 1, value[1]]


def get_value(maze):
    pass


def get_x(maze):
    x = 0

    for line in maze:
        x += 1

    return x


def get_y(maze):
    x = 0
    y = 0

    for line in maze:
        x += 1
        for key in line:
            y += 1

    return y // x


def is_valid(value, valid):
    pass

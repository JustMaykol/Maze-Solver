W = '#'
B = ' '

S = 'S'
E = 'E'


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
    return [get_x(maze), get_y(maze)]


def get_x(maze):
    x = 0

    for _ in maze:
        x += 1

    return x


def get_y(maze):
    x = 0
    y = 0

    for line in maze:
        x += 1
        for _ in line:
            y += 1

    return y // x


def is_valid(value, valid):
    return -1 < value[0] < valid[0] and -1 < value[1] < valid[1]


def is_wall(maze, value):
    return maze[value[0]][value[1]] == W


def is_blank(maze, value):
    return maze[value[0]][value[1]] == B


def is_start(maze, value):
    return maze[value[0]][value[1]] == S


def is_end(maze, value):
    return maze[value[0]][value[1]] == E

W = '#'
B = ' '

S = 'S'
E = 'E'


def find_start(maze):
    for a, line in enumerate(maze):
        for b, key in enumerate(line):
            if key == S:
                return [a, b]


def find_end(maze):
    for a, line in enumerate(maze):
        for b, key in enumerate(line):
            if key == E:
                return [a, b]


def is_wall(maze, value):
    return maze[value[0]][value[1]] == W


def is_blank(maze, value):
    return maze[value[0]][value[1]] == B


def is_start(maze, value):
    return maze[value[0]][value[1]] == S


def is_end(maze, value):
    return maze[value[0]][value[1]] == E

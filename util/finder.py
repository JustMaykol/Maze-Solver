from util import position

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


def find_path(maze):
    i = 0

    path = []
    temp = []

    start = find_start(maze)
    end = find_end(maze)

    value = position.get_value(maze)

    path.append(start)

    while True:
        found = any(item for item in position.get_near(end) if item in path)

        if found:
            break

        i += 1

        for key in path:
            for way in position.get_near(key):
                if position.is_valid(way, value):
                    if position.is_blank(maze, way):
                        maze[way[0]][way[1]] = i
                        temp.append(way)
                    elif position.is_end(maze, way):
                        temp.append(way)

        path.clear()

        for key in temp:
            path.append(key)

        temp.clear()

    return i


def find_way(maze, i):
    path = []

    start = find_start(maze)
    end = find_end(maze)

    value = position.get_value(maze)

    key = end

    while True:
        if key == start:
            break

        for way in position.get_near(key):
            if position.is_valid(way, value):
                if isinstance(maze[way[0]][way[1]], int):
                    if maze[way[0]][way[1]] == i:
                        maze[way[0]][way[1]] = 'o'
                        path.append(way)
                        key = way
                        i -= 1
                elif position.is_start(maze, way):
                    key = way

    return path

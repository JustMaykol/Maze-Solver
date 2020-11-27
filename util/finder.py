def find_start(maze):
    for a, line in enumerate(maze):
        for b, key in enumerate(line):
            if key == 'S':
                return [a, b]


def find_end(maze):
    for a, line in enumerate(maze):
        for b, key in enumerate(line):
            if key == 'E':
                return [a, b]

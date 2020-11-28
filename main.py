from util import finder
from util import printer
from util import position

W = '#'
B = ' '

S = 'S'
E = 'E'

path = []

test = [['#', '#', '#', 'E', '#'],
        ['#', ' ', ' ', ' ', '#'],
        ['#', ' ', 'S', ' ', '#'],
        ['#', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#']]


def solve_maze(maze):
    start = finder.find_start(maze)
    end = finder.find_end(maze)

    value = position.get_value(maze)

    path.append(start)

    while True:
        for key in path:
            if position.is_valid(key, value):
                for way in position.get_near(key):
                    if position.is_valid(way, value):
                        if finder.is_blank(maze, way):
                            print(way)


def main():
    solve_maze(test)


if __name__ == '__main__':
    main()

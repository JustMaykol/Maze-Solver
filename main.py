from util import finder
from util import printer
from util import position

W = '#'
B = ' '

S = 'S'
E = 'E'

path = []


def solve_maze(maze):
    start = finder.find_start(maze)
    end = finder.find_end(maze)

    value = position.get_value(maze)

    while True:
        path.clear()


def main():
    pass


if __name__ == '__main__':
    main()

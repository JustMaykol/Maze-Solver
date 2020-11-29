from util import finder
from util import printer
from util import position

W = '#'
B = ' '

S = 'S'
E = 'E'

test = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['S', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        ['#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#'],
        ['#', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', 'E'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]


def solve_maze(maze):
    index = finder.find_path(maze)
    path = finder.find_way(maze, index)

    for x, line in enumerate(maze):
        for y, string in enumerate(line):
            if isinstance(maze[x][y], int):
                maze[x][y] = ' '

    return path


def main():
    print(solve_maze(test))
    printer.print_maze(test)


if __name__ == '__main__':
    main()

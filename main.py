WALL = '#'
BLANK = ' '

START = 'S'
END = 'E'

maze = [['#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#']]


def printMaze(value):
    for line in value:
        for key in line:
            print(key, end=' ')
        print(' ')


print(getNear([2, 2]))

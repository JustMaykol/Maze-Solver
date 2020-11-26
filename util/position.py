# Up, Right, Down, Left
def getNear(x, y):
    return [getUp(x, y), getRight(x, y), getDown(x, y), ]


def getUp(x, y):
    return [x, y - 1]


def getRight(x, y):
    return [x + 1, y]


def getDown(x, y):
    return [x, y + 1]


def getLeft(x, y):
    return [x - 1, y]

# Up, Right, Down, Left
def get_near(x, y):
    return [get_up(x, y), get_right(x, y), get_down(x, y), get_left(x, y)]


def get_up(x, y):
    return [x, y - 1]


def get_right(x, y):
    return [x + 1, y]


def get_down(x, y):
    return [x, y + 1]


def get_left(x, y):
    return [x - 1, y]

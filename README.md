# Maze Solver

This is a **Maze Solver** based on **Python** and without the use of any external library, the idea of the program is to
enter a matrix (list of lists) with the maze and this will return the maze already solved, and the way the program
follow.

## Usage

You can clone this repository and join a matrix with the maze.

## Example

Here is an example how you can join a matrix to the solver.

```python
from util import finder
from util import printer
from util import position

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
```

Here the expected output.

```text
[[9, 8], [9, 7], [9, 6], [9, 5], [9, 4], [9, 3], [8, 3], [7, 3], [7, 2], [7, 1], [6, 1], [5, 1], [4, 1], [3, 1], [2, 1], [1, 1]]
# # # # # # # # # #  
S o #             #  
# o # # #   # #   #  
# o     #   #     #  
# o #       #     #  
# o # # #   # # # #  
# o #             #  
# o o o #   # # # #  
#   # o #     #   #  
#   # o o o o o o E  
# # # # # # # # # #  

Process finished with exit code 0

```
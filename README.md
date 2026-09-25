# Maze Solver

Finds the **shortest path** in a grid maze using Lee's algorithm (wavefront breadth-first search). Written in Python, with no dependencies.

## Maze format

A list of lists of characters:

| Character | Meaning |
|---|---|
| `#` | Wall |
| ` ` | Open cell |
| `S` | Start |
| `E` | Exit |

## Usage

```python
from main import solve_maze
from util.printer import print_maze

maze = [list(row) for row in [
    "##########",
    "#S   #   #",
    "# ## # # #",
    "#  #   # #",
    "## ##### #",
    "#       E#",
    "##########",
]]

path = solve_maze(maze)
print_maze(maze)
print("steps:", len(path))
```

The path is marked with `o` inside the maze itself:

```
# # # # # # # # # #
# S       #       #
# o # #   #   #   #
# o o #       #   #
# # o # # # # #   #
#   o o o o o o E #
# # # # # # # # # #
steps: 10
```

## How it works

1. **Expansion** (`finder.find_path`): starting from `S`, it numbers each open cell with its distance (1, 2, 3…), moving in 4 directions until it reaches the cell next to `E`.
2. **Backtracking** (`finder.find_way`): starting from `E`, it follows the cells with decreasing distance back to `S`, marking them with `o`.

## Structure

```
main.py            # solve_maze()
util/
├── finder.py      # expansion and backtracking
├── position.py    # neighbors, bounds and cell type
└── printer.py     # print_maze()
```

## Edge cases

- If the exit is unreachable, `solve_maze` returns an empty list.

## Requirements

- The maze must be rectangular (every row must have the same length).

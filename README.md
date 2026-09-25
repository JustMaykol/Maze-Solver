# Maze Solver

Encuentra el **camino más corto** en un laberinto de cuadrícula usando el algoritmo de Lee (búsqueda en anchura por frentes de onda). Escrito en Python, sin dependencias.

## Formato del laberinto

Una lista de listas de caracteres:

| Carácter | Significado |
|---|---|
| `#` | Pared |
| ` ` | Espacio libre |
| `S` | Inicio |
| `E` | Salida |

## Uso

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
print("pasos:", len(path))
```

El camino queda marcado con `o` dentro del mismo laberinto:

```
# # # # # # # # # #
# S       #       #
# o # #   #   #   #
# o o #       #   #
# # o # # # # #   #
#   o o o o o o E #
# # # # # # # # # #
pasos: 10
```

## Cómo funciona

1. **Expansión** (`finder.find_path`): desde `S`, numera cada celda libre con su distancia (1, 2, 3…), avanzando en las 4 direcciones hasta llegar al lado de `E`.
2. **Retroceso** (`finder.find_way`): desde `E`, sigue las celdas con distancia decreciente hasta volver a `S`, marcándolas con `o`.

## Estructura

```
main.py            # solve_maze()
util/
├── finder.py      # expansión y retroceso
├── position.py    # vecinos, límites y tipo de celda
└── printer.py     # print_maze()
```

## Limitaciones

- Si el laberinto **no tiene salida alcanzable**, la búsqueda no termina (bucle infinito).
- El laberinto debe ser rectangular (todas las filas del mismo largo).

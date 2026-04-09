# Referencia de la API interna

## `a_maze_ing.py`

### `ft_make_maze() -> None`
Función principal. Lee `sys.argv[1]` como ruta al config, parsea la configuración y ejecuta el flujo completo (generación o carga desde semilla).

### `export_maze_to_file(maze, string_directions, maze_config) -> None`
Genera la semilla hex del laberinto y la exporta al archivo de salida.

| Parámetro          | Tipo          | Descripción |
|--------------------|---------------|-------------|
| `maze`             | `Maze`        | Laberinto generado |
| `string_directions`| `str`         | Cadena de direcciones de la solución |
| `maze_config`      | `ConfigModel` | Configuración con la ruta de salida |

---

## `src/model/cell.py`

### `class Cell`

| Atributo        | Tipo              | Descripción |
|-----------------|-------------------|-------------|
| `x`             | `int`             | Coordenada horizontal |
| `y`             | `int`             | Coordenada vertical |
| `visited`       | `bool`            | Marcada durante generación o resolución |
| `is_FORTY_TWO`  | `bool`            | Pertenece al patrón "42" |
| `is_start`      | `bool`            | Es la celda de entrada |
| `is_exit`       | `bool`            | Es la celda de salida |
| `walls`         | `dict[str, bool]` | Estado de paredes: `{"N": True, "S": True, "E": True, "W": True}` |

---

## `src/model/maze.py`

### `class Maze`

#### `__init__(maze_config: ConfigModel)`
Inicializa el laberinto con dimensiones del config. Crea la instancia de `BuiltMaze`.

#### `initial_matrix() -> List[List[Cell]]`
Crea el grid 2D de celdas. Debe llamarse antes de generar el laberinto.

#### `generate_seed() -> List[List[str]]`
Convierte el grid a representación hex. Cada celda → un carácter hex (0-F).

#### `export_seed(maze_seed, solve_directions, maze_config) -> None`
Escribe el laberinto en `./output/<maze_output>`. Crea el directorio si no existe. Valida que la ruta no salga de `./output/`.

---

### `class Maze.BuiltMaze`

#### `is_within_bounds(x, y) -> bool`
Verifica que las coordenadas estén dentro del grid.

#### `get_cell(x, y) -> Optional[Cell]`
Devuelve la celda en `(x, y)` o `None` si está fuera de límites.

#### `get_directions() -> list[tuple[str, int, int]]`
Devuelve `[("N", 0, -1), ("E", 1, 0), ("S", 0, 1), ("W", -1, 0)]`.

#### `opposite_wall(wall: str) -> str`
Devuelve la pared opuesta: N↔S, E↔W.

#### `get_neighbors(cell) -> List[tuple[Cell, str]]`
Devuelve vecinos no visitados con la dirección de la pared que los separa.

#### `has_necessary_dimensions() -> bool`
`True` si `width >= 9` y `height >= 7` (necesario para el watermark).

#### `watermark() -> bool`
Marca las celdas del patrón "42" como `is_FORTY_TWO = True` y `visited = True`.

#### `check_valid_position(start, exit) -> bool`
Valida que las coordenadas existan y no coincidan con celdas del watermark.

#### `open_areas(max_passes=10) -> None`
Elimina zonas abiertas 2×3 o 3×2 añadiendo paredes con huecos aleatorios.

#### `perfect_maze(start, exit, is_perfect=True, algorithm=DFS) -> None`
Genera el laberinto completo:
1. Inicializa el grid si está vacío
2. Aplica `random.seed(self.maze.seed_code)`
3. Marca start/exit
4. Aplica watermark
5. Ejecuta DFS o Prim
6. Si `is_perfect=False`, elimina paredes adicionales
7. Llama a `open_areas()`

#### `solve_maze(start, exit, reg_solve=True) -> str`
Resuelve el laberinto con BFS. Si `reg_solve=False` y ya existe una solución cacheada en `maze.solve_maze_seed`, la devuelve directamente.

#### `get_cells_solve_maze(start, exit) -> Optional[List[Cell]]`
BFS puro. Devuelve la lista de celdas del camino o `None` si no hay solución.

#### `path_to_directions(path) -> str`
Convierte lista de celdas a cadena de caracteres `N/S/E/W`.

---

## `src/model/seed.py`

### `class Seed`

#### `__init__(maze_config: ConfigModel)`
Inicializa con la configuración. `seed_config` y `grid_seed` empiezan vacíos.

#### `get_cell(x, y) -> Optional[Cell]`
Devuelve la celda del grid de semilla en `(x, y)`.

#### `validate_solution() -> bool`
Verifica la consistencia de paredes entre celdas adyacentes en el archivo de semilla. Termina el programa si el archivo es inválido.

#### `get_seed_info() -> None`
Lee el archivo de semilla, extrae el hex del laberinto y los metadatos (entry, exit, solución). Construye el grid vacío de celdas.

#### `create_grid_from_seed() -> None`
Aplica los estados de paredes a cada celda según su valor hex. Detecta celdas `is_FORTY_TWO` (todas las paredes cerradas). Lanza `SeedPainter_ascii`.

#### `get_solution_coord() -> set[tuple[int, int]]`
Convierte la cadena de solución del seed_config a un conjunto de coordenadas.

---

## `src/parser/config_model.py`

### `class ConfigModel(BaseModel)`

| Campo            | Tipo           | Restricción | Descripción |
|------------------|----------------|-------------|-------------|
| `maze_width`     | `int`          | `>= 3`      | Ancho |
| `maze_height`    | `int`          | `>= 3`      | Alto |
| `maze_entry`     | `tuple[int,int]`| dentro de límites | Entrada |
| `maze_exit`      | `tuple[int,int]`| dentro de límites, ≠ entry | Salida |
| `maze_output`    | `str`          | `len >= 5`  | Archivo de salida |
| `maze_perfect`   | `bool`         | —           | Laberinto perfecto |
| `maze_print_mode`| `str`          | `ASCII` o `MLX` | Modo de visualización |
| `maze_seed`      | `str`          | default `""` | Ruta a semilla |
| `maze_seed_code` | `int \| None`  | default `None` | Código de semilla |

---

## `src/parser/ft_parser_config.py`

### `config_adapter(maze_config: dict) -> dict`
Transforma las claves del archivo de config al esquema de `ConfigModel`. Convierte tipos (int, tuple, bool, str). Genera `maze_seed_code` aleatorio si está vacío.

### `ft_parsing_config(config_file: str) -> ConfigModel`
Lee el archivo, llama a `config_adapter()` y valida con Pydantic. Termina con `sys.exit(1)` en cualquier error.

---

## `src/visual/print_ascii.py`

### `class MazePainter_ascii`

#### `__init__(maze, maze_config)`
Inicializa con colores blancos y `show_solution=False`.

#### `get_solution_coord() -> set[tuple[int, int]]`
Resuelve el laberinto y convierte la cadena de direcciones a coordenadas.

#### `print_maze_ascii() -> None`
Renderiza el laberinto con caracteres Unicode de caja. Muestra solución, start y exit con colores ANSI.

#### `draw_maze_by_op(maze_color, pattern_color, algorithm=DFS) -> None`
Regenera el laberinto con el algoritmo y colores indicados.

#### `animate_colored_mazes(delay=0.005) -> None`
Genera laberintos con cada color disponible con un delay entre cada uno.

#### `put_parameters() -> None`
Bucle interactivo del menú de terminal.

#### `start_visual() -> None`
Renderiza y lanza el menú interactivo.

---

## `src/visual/print_minilib.py`

### `class MazePainter_mlx`

#### `create_window() -> None`
Crea la ventana MLX. Dimensiones: `width * cell_size` × `(height * cell_size) + 280`.

#### `create_image() / create_solution_img() -> None`
Crean los buffers de imagen para el laberinto y la solución.

#### `put_pixel_img(x, y, color, img) -> None`
Escribe un píxel en el buffer de imagen.

#### `cell_pixel_put(cell, x, y, color) -> None`
Dibuja una celda completa: paredes, marcas de start/exit, patrón "42".

#### `start_pixel_put(color) -> None`
Dibuja todas las celdas del grid con el color indicado.

#### `draw_maze_by_op(maze_color, pattern_color, param, algorithm=DFS) -> None`
Regenera y redibuja el laberinto.

#### `render(param) -> None`
Renderiza el frame actual si `needs_redraw=True`.

#### `start_visual() -> None`
Crea ventana, imagen, hooks de eventos y lanza el loop MLX.

---

## `src/visual/print_seed_ascii.py`

### `class SeedPainter_ascii`

#### `__init__(seed, seed_config)`
Inicializa con `show_solution=True` por defecto.

#### `print_maze_ascii() -> None`
Renderiza el laberinto de la semilla con la solución visible.

#### `start_visual() -> None`
Limpia la pantalla y renderiza. Sin menú interactivo.

---

## `src/config/enums.py`

### `Colors` — ANSI para terminal
`RESET, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE`

### `ColorsHex` — 0xAARRGGBB para MLX
`WHITE, BLACK, RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, GRAY, ORANGE, PURPLE, BROWN, PINK, LIME`

### `Walls`
`N = "N"`, `S = "S"`, `E = "E"`, `W = "W"`

### `PrintMode`
`MLX = "MLX"`, `ASCII = "ASCII"`

### `MazeAlgorithm`
`DFS = "DFS"`, `PRIM = "PRIM"`

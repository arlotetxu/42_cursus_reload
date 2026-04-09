# A-Maze-ing — Visión general del proyecto

Generador y visualizador de laberintos procedurales desarrollado como parte del currículo de 42 School.

## Funcionalidades principales

- Generación de laberintos perfectos e imperfectos mediante DFS o Prim
- Resolución automática con BFS (camino más corto)
- Visualización en terminal (ASCII) o ventana gráfica (MLX)
- Exportación del laberinto a archivo de semilla (hex)
- Carga y reproducción de laberintos desde semilla
- Marca de agua "42" integrada en el centro del laberinto

## Flujo de ejecución

```
a-maze-ing config.txt
        │
        ▼
ft_parsing_config()          ← lee y valida config.txt con Pydantic
        │
        ├── maze_seed vacío
        │       │
        │       ▼
        │   Maze(maze_config)
        │   maze.build.perfect_maze()   ← DFS o Prim
        │   maze.build.solve_maze()     ← BFS
        │   export_maze_to_file()       ← escribe ./output/<archivo>
        │   MazePainter_ascii / MazePainter_mlx
        │
        └── maze_seed = "ruta/archivo"
                │
                ▼
            Seed(maze_config)
            seed.create_grid_from_seed()   ← parsea hex, reconstruye grid
            SeedPainter_ascii              ← visualiza en terminal
```

## Estructura de directorios

```
a-maze-ing/
├── a_maze_ing.py          # Entry point
├── config.txt             # Configuración por defecto
├── pyproject.toml         # Metadatos y dependencias
├── Makefile
├── inc/mlx/               # Librería gráfica MLX (binario incluido)
├── src/
│   ├── config/
│   │   └── enums.py       # Colors, ColorsHex, Walls, PrintMode, MazeAlgorithm
│   ├── model/
│   │   ├── cell.py        # Clase Cell
│   │   ├── maze.py        # Clase Maze + BuiltMaze
│   │   └── seed.py        # Clase Seed (carga desde archivo)
│   ├── parser/
│   │   ├── config_model.py        # Modelo Pydantic
│   │   └── ft_parser_config.py    # Parser del config.txt
│   └── visual/
│       ├── print_ascii.py         # MazePainter_ascii
│       ├── print_minilib.py       # MazePainter_mlx
│       └── print_seed_ascii.py    # SeedPainter_ascii
├── tests/
│   ├── test_a_maze_ing.py
│   ├── test_parser_config.py
│   └── tests.py
└── context/               # Documentación técnica (este directorio)
```

## Versión y dependencias

| Paquete       | Versión mínima |
|---------------|----------------|
| Python        | 3.10           |
| pydantic      | 2.12.5         |
| pytest        | 9.0.2          |
| pytest-mock   | 3.15.1         |
| flake8        | 7.3.0          |
| mypy          | 1.19.1         |
| pre-commit    | 4.5.1          |

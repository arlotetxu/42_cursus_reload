# Arquitectura del proyecto

## Capas

```
┌─────────────────────────────────────────┐
│              Entry Point                │
│           a_maze_ing.py                 │
└────────────────┬────────────────────────┘
                 │
     ┌───────────┴───────────┐
     │                       │
     ▼                       ▼
┌─────────┐           ┌────────────┐
│  Parser │           │    Seed    │
│  Layer  │           │   Loader   │
└────┬────┘           └─────┬──────┘
     │                      │
     ▼                      ▼
┌──────────────┐    ┌───────────────┐
│  ConfigModel │    │  Seed class   │
│  (Pydantic)  │    │  seed.py      │
└──────┬───────┘    └───────┬───────┘
       │                    │
       ▼                    ▼
┌──────────────────────────────────┐
│         Maze Generator           │
│   Maze + BuiltMaze (maze.py)     │
│   Cell (cell.py)                 │
└──────────────┬───────────────────┘
               │
     ┌─────────┴──────────┐
     │                    │
     ▼                    ▼
┌──────────┐      ┌───────────────┐
│  ASCII   │      │  MLX (gráfico)│
│ Renderer │      │   Renderer    │
└──────────┘      └───────────────┘
```

## Módulos y responsabilidades

### `a_maze_ing.py`
Punto de entrada. Orquesta el flujo completo:
1. Parsea argumentos de línea de comandos
2. Delega la configuración al parser
3. Decide entre flujo de generación o flujo de semilla
4. Instancia el renderer adecuado

### `src/parser/`

**`ft_parser_config.py`**
- Lee el archivo de configuración línea a línea (`KEY=VALUE`)
- `config_adapter()` transforma las claves al esquema de `ConfigModel`
- Maneja errores de tipo y formato antes de la validación Pydantic

**`config_model.py`**
- Modelo Pydantic con validación declarativa
- Validadores de negocio: coordenadas dentro de límites, entry ≠ exit, modo de impresión válido, límite de recursión (width × height < 1000)

### `src/model/`

**`cell.py`**
- Unidad mínima del laberinto
- Almacena coordenadas, estado de visita, paredes (N/S/E/W), flags especiales (`is_start`, `is_exit`, `is_FORTY_TWO`)

**`maze.py`**
- `Maze`: contenedor del grid y metadatos
- `Maze.BuiltMaze`: clase anidada con toda la lógica de construcción y resolución
  - Generación: DFS recursivo, Prim iterativo
  - Resolución: BFS iterativo
  - Watermark "42": marca celdas pre-visitadas en el centro
  - `open_areas()`: elimina zonas abiertas 2×3 o 3×2 añadiendo paredes
  - `export_seed()`: escribe el laberinto en formato hex en `./output/`

**`seed.py`**
- `Seed`: carga un laberinto desde un archivo de semilla hex
- `validate_solution()`: verifica consistencia de paredes entre celdas adyacentes
- `get_seed_info()`: parsea el archivo y construye el grid
- `create_grid_from_seed()`: aplica estados de paredes y lanza `SeedPainter_ascii`

### `src/visual/`

**`print_ascii.py` — `MazePainter_ascii`**
- Renderiza el laberinto con caracteres de caja Unicode (`┌ ─ ┬ │ ┼ └`)
- Menú interactivo en terminal: regenerar, mostrar solución, cambiar colores, animar
- `animate_colored_mazes()`: genera varios laberintos con colores distintos con delay

**`print_minilib.py` — `MazePainter_mlx`**
- Renderiza el laberinto píxel a píxel usando la librería MLX
- Gestión de eventos de teclado y ventana
- Animación de colores basada en tiempo (`time.monotonic()`)
- Doble buffer de imagen: uno para el laberinto, otro para la solución

**`print_seed_ascii.py` — `SeedPainter_ascii`**
- Renderer de solo lectura para laberintos cargados desde semilla
- Muestra la solución automáticamente (`show_solution = True` por defecto)
- Sin menú interactivo (versión simplificada de `MazePainter_ascii`)

### `src/config/enums.py`
Centraliza todas las constantes del proyecto:
- `Colors`: códigos ANSI para terminal
- `ColorsHex`: colores en formato 0xAARRGGBB para MLX
- `Walls`: direcciones cardinales (N/S/E/W)
- `PrintMode`: ASCII / MLX
- `MazeAlgorithm`: DFS / PRIM

## Formato del archivo de semilla

```
<fila_hex_0>
<fila_hex_1>
...
<fila_hex_N>
                    ← línea vacía como separador
<entry_x>,<entry_y>
<exit_x>,<exit_y>
<cadena_de_direcciones>
```

Cada carácter hex codifica las paredes de una celda:

| Bit | Pared | Valor |
|-----|-------|-------|
| 0   | Norte | 1     |
| 1   | Este  | 2     |
| 2   | Sur   | 4     |
| 3   | Oeste | 8     |

Ejemplo: `C` = 0xC = 12 = `1100b` → paredes Sur y Oeste presentes.

## Restricciones de diseño

| Restricción | Valor | Motivo |
|-------------|-------|--------|
| `width × height` | < 1000 | Evitar `RecursionError` en DFS |
| `width` mínimo | 3 | Validación Pydantic |
| `height` mínimo | 3 | Validación Pydantic |
| Watermark "42" | requiere width ≥ 9, height ≥ 7 | Espacio para el patrón |
| Output path | debe estar bajo `./output/` | Prevención de path traversal |

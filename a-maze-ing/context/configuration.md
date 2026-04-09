# Configuración

## Formato del archivo de configuración

El archivo de configuración usa el formato `CLAVE=VALOR`, una por línea.
Las líneas sin `=` se ignoran (útil para comentarios con `#`).
Los espacios alrededor de la clave y el valor se eliminan automáticamente.

```ini
WIDTH=30
HEIGHT=25
ENTRY=0,0
EXIT=13,22
OUTPUT_FILE=output_maze.txt
PERFECT=false
PRINT_MODE=mlx
SEED=
SEED_CODE=
```

## Parámetros

| Clave         | Tipo    | Requerido | Descripción |
|---------------|---------|-----------|-------------|
| `WIDTH`       | int     | Sí        | Ancho del laberinto en celdas. Mínimo: 3 |
| `HEIGHT`      | int     | Sí        | Alto del laberinto en celdas. Mínimo: 3 |
| `ENTRY`       | x,y     | Sí        | Coordenadas del punto de entrada |
| `EXIT`        | x,y     | Sí        | Coordenadas del punto de salida (≠ ENTRY) |
| `OUTPUT_FILE` | string  | Sí        | Nombre del archivo de salida (mínimo 5 caracteres). Se guarda en `./output/` |
| `PERFECT`     | bool    | Sí        | `true` = laberinto perfecto (un solo camino). `false` = imperfecto (con ciclos) |
| `PRINT_MODE`  | string  | Sí        | Modo de visualización: `ascii` o `mlx` |
| `SEED`        | string  | No        | Ruta al archivo de semilla para reproducir un laberinto. Vacío = generar nuevo |
| `SEED_CODE`   | int     | No        | Código numérico para reproducir el mismo laberinto. Vacío = aleatorio |

## Validaciones aplicadas

- `WIDTH` y `HEIGHT` deben ser ≥ 3
- `WIDTH × HEIGHT` debe ser < 1000 (límite de recursión)
- Las coordenadas de `ENTRY` y `EXIT` deben estar dentro de los límites del laberinto
- `ENTRY` y `EXIT` no pueden ser iguales
- `PRINT_MODE` debe ser `ASCII` o `MLX` (insensible a mayúsculas)
- `OUTPUT_FILE` debe tener al menos 5 caracteres
- La ruta de salida debe estar bajo `./output/` (prevención de path traversal)

## Comportamiento del SEED_CODE

- Si `SEED_CODE` está vacío o ausente, se genera un número aleatorio entre 1 y 50000
- Este código se usa como semilla de `random.seed()` durante la generación, lo que hace el laberinto reproducible
- El código se muestra en el menú interactivo para que pueda ser reutilizado

## Ejemplos de configuración

### Laberinto pequeño perfecto en ASCII
```ini
WIDTH=20
HEIGHT=10
ENTRY=0,0
EXIT=19,9
OUTPUT_FILE=small_output.txt
PERFECT=true
PRINT_MODE=ascii
SEED=
SEED_CODE=
```

### Laberinto grande imperfecto en MLX
```ini
WIDTH=30
HEIGHT=25
ENTRY=0,0
EXIT=29,24
OUTPUT_FILE=large_output.txt
PERFECT=false
PRINT_MODE=mlx
SEED=
SEED_CODE=
```

### Reproducir un laberinto desde semilla
```ini
WIDTH=10
HEIGHT=10
ENTRY=0,0
EXIT=9,9
OUTPUT_FILE=replay.txt
PERFECT=true
PRINT_MODE=ascii
SEED=output/large_output.txt
SEED_CODE=
```

## Mapeo interno de claves

El parser transforma las claves del archivo al esquema de `ConfigModel`:

| Config file   | ConfigModel field  |
|---------------|--------------------|
| `WIDTH`       | `maze_width`       |
| `HEIGHT`      | `maze_height`      |
| `ENTRY`       | `maze_entry`       |
| `EXIT`        | `maze_exit`        |
| `OUTPUT_FILE` | `maze_output`      |
| `PERFECT`     | `maze_perfect`     |
| `PRINT_MODE`  | `maze_print_mode`  |
| `SEED`        | `maze_seed`        |
| `SEED_CODE`   | `maze_seed_code`   |

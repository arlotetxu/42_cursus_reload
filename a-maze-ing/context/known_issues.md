# Problemas conocidos y deuda técnica

## Bugs confirmados

### `tests/tests.py::TestCases::test_f` — test roto
```python
def test_f(self):
    with pytest.raises(ValueError):
        self.raising_error(10)  # ← no lanza ValueError, devuelve 10.0
```
`raising_error` solo lanza `ValueError` cuando `div == 0`. Con `div=10` devuelve `10.0`.
**Fix:** cambiar `self.raising_error(10)` por `self.raising_error(0)`.

---

## Problemas de diseño

### Import local dentro de método (`seed.py`)
```python
def create_grid_from_seed(self) -> None:
    ...
    from src.visual.print_seed_ascii import SeedPainter_ascii  # ← import local
    seed_ascii_painter = SeedPainter_ascii(self, self.seed_config)
```
El import local evita una dependencia circular pero oculta la dependencia real.
**Alternativa:** reestructurar para que el entry point (`a_maze_ing.py`) instancie el renderer, igual que hace con `MazePainter_ascii`.

### `BuiltMaze` como clase anidada en `Maze`
Toda la lógica de generación y resolución vive en una clase anidada de 1000+ líneas.
Dificulta el testing unitario de los algoritmos de forma aislada.
**Alternativa:** extraer `BuiltMaze` a su propio módulo `src/model/builder.py`.

### Archivo `maze.py` de 1197 líneas
Demasiado grande para un solo archivo. Mezcla la clase contenedora, la lógica de generación, la resolución y la exportación.

### Modo semilla solo soporta ASCII
Cuando `SEED` tiene valor, `create_grid_from_seed()` siempre lanza `SeedPainter_ascii`, ignorando `PRINT_MODE`.
Si el usuario configura `PRINT_MODE=mlx` con una semilla, el comportamiento no es el esperado.

---

## Problemas de rendimiento

### Doble lectura del archivo de semilla
`validate_solution()` y `get_seed_info()` abren el mismo archivo por separado.
**Fix:** leer el archivo una sola vez y pasar los datos a ambas funciones.

### BFS llamado múltiples veces
En el flujo normal, `solve_maze()` se llama en `ft_make_maze()` y potencialmente de nuevo en `get_solution_coord()` del renderer.
El parámetro `reg_solve` existe para cachear la solución pero no se usa de forma consistente.

### Renderizado píxel a píxel en MLX
`cell_pixel_put()` itera píxel a píxel con bucles Python anidados. Para laberintos grandes esto es lento.

---

## Limitaciones conocidas

### Límite de recursión en DFS
`width × height < 1000` es una restricción dura. Para laberintos de 31×32 o más, el DFS puede causar `RecursionError`.
Prim no tiene este problema al ser iterativo.

### `maze_perfect` acepta strings como booleanos
Pydantic convierte `"false"` a `True` por defecto con `bool`. El parser no hace coerción explícita.
```ini
PERFECT=false  # → maze_perfect = True (incorrecto)
```
**Fix:** en `config_adapter()`, convertir explícitamente: `maze_config["maze_perfect"] = value.lower() == "true"`.

### Validación de `SEED_CODE` en `ConfigModel`
`SEED_CODE` vacío genera un número aleatorio en el parser, pero si se pasa directamente a `ConfigModel` sin pasar por `config_adapter()`, el campo queda como `None`.

### Tamaño mínimo de ventana MLX
`create_window()` fuerza `maze_width = 12` si es menor, sin notificar al usuario:
```python
if self.maze_width < 12:
    self.maze_width = 12
```
Esto puede causar inconsistencias entre el laberinto generado y la ventana mostrada.

---

## Mejoras sugeridas

| Área | Mejora |
|------|--------|
| `seed.py` | Eliminar import local, pasar renderer como parámetro |
| `maze.py` | Extraer `BuiltMaze` a módulo separado |
| `ft_parser_config.py` | Coerción explícita de `PERFECT` a bool |
| `seed.py` | Leer el archivo de semilla una sola vez |
| `print_seed_ascii.py` | Añadir menú interactivo o soporte MLX |
| `tests/` | Añadir tests para `Maze`, `Seed`, algoritmos y renderers |
| `maze.py` | Cachear la solución de forma consistente |
| `tests/tests.py` | Corregir `test_f` |

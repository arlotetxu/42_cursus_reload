# Testing

## Ejecutar los tests

```bash
# Todos los tests
uv run pytest

# Con verbose
uv run pytest -v

# Un archivo específico
uv run pytest tests/test_a_maze_ing.py

# Un test específico
uv run pytest tests/test_a_maze_ing.py::test_ft_make_maze_ascii_mode
```

## Estructura de tests

```
tests/
├── test_a_maze_ing.py     # Tests del entry point y flujo principal
├── test_parser_config.py  # Tests del parser de configuración
└── tests.py               # Placeholder (contiene un test roto)
```

---

## `test_a_maze_ing.py`

Cubre el flujo principal de `ft_make_maze()` y `export_maze_to_file()` usando mocks.

### Fixtures

**`mock_config`**
Mock de `ConfigModel` con valores por defecto:
- `maze_width=10`, `maze_height=10`
- `maze_entry=(0,0)`, `maze_exit=(9,9)`
- `maze_perfect=True`
- `maze_print_mode=PrintMode.ASCII.value`
- `maze_seed=""`

**`mock_maze`**
Mock de `Maze` con:
- `build.perfect_maze` → Mock
- `build.solve_maze` → devuelve `"UDLR"`
- `generate_seed` → devuelve `[[]]`
- `export_seed` → Mock

### Tests

| Test | Qué verifica |
|------|-------------|
| `test_ft_make_maze_ascii_mode` | Flujo completo en modo ASCII: parsing, instanciación de Maze con config, llamada a perfect_maze, export y start_visual |
| `test_ft_make_maze_mlx_mode` | Flujo completo en modo MLX: start_visual del painter MLX |
| `test_ft_make_maze_calls_perfect_maze` | perfect_maze se llama con `(0,0), (9,9), True` |
| `test_ft_make_maze_calls_solve_maze` | solve_maze se llama con `(0,0), (9,9)` |
| `test_export_maze_to_file` | generate_seed y export_seed se llaman con los parámetros correctos |
| `test_ft_make_maze_seed_mode` | Cuando `maze_seed` tiene valor, se instancia `Seed` y se llama `create_grid_from_seed()` |

---

## `test_parser_config.py`

Cubre `ft_parsing_config()` con archivos temporales (`tmp_path`) y mocks.

### Tests

| Test | Qué verifica |
|------|-------------|
| `test_valid_config_file` | Config válido → `ConfigModel` con valores correctos |
| `test_empty_config_file_path` | Path vacío → usa `config.txt` por defecto |
| `test_file_not_found` | Archivo inexistente → `sys.exit(1)` con `[ERROR]` en stdout |
| `test_invalid_width_type` | `WIDTH=invalid` → `sys.exit(1)` con `[ERROR]` |
| `test_invalid_entry_format` | `ENTRY=invalid` → `sys.exit(1)` |
| `test_pydantic_validation_error` | `WIDTH=-5` → `sys.exit(1)` |
| `test_key_value_parsing` | Parseo correcto de WIDTH, HEIGHT, OUTPUT_FILE |
| `test_print_mode_uppercase_conversion` | `PRINT_MODE=console` → `maze_print_mode="CONSOLE"` |
| `test_skip_lines_without_equals` | Líneas sin `=` se ignoran |
| `test_whitespace_trimming` | Espacios alrededor de clave y valor se eliminan |
| `test_config_without_seed_defaults_to_empty` | Sin `SEED` → `maze_seed=""` |
| `test_config_with_seed_is_parsed` | `SEED=output/seed1.txt` → `maze_seed="output/seed1.txt"` |

---

## Cobertura actual

| Módulo | Cobertura |
|--------|-----------|
| `a_maze_ing.py` | Alta (flujo principal mockeado) |
| `ft_parser_config.py` | Alta (casos válidos e inválidos) |
| `config_model.py` | Media (cubierto indirectamente por parser tests) |
| `maze.py` | Baja (sin tests unitarios directos) |
| `cell.py` | Sin tests |
| `seed.py` | Sin tests |
| `print_ascii.py` | Sin tests |
| `print_minilib.py` | Sin tests |
| `print_seed_ascii.py` | Sin tests |

## Tests conocidos con problemas

**`tests/tests.py::TestCases::test_f`**
```python
def test_f(self):
    with pytest.raises(ValueError):
        self.raising_error(10)  # 100/10 = 10.0, no lanza ValueError
```
Este test falla porque `raising_error(10)` no lanza `ValueError` (solo lo hace con `div=0`).

## Áreas sin cobertura de tests

- Algoritmos de generación (DFS, Prim) — propiedades de correctness
- Solver BFS — verificación de camino mínimo
- Clase `Seed` — parsing de semilla, validación de paredes
- Renderers ASCII y MLX — difíciles de testear sin display
- `open_areas()` — eliminación de zonas abiertas
- Watermark "42" — posicionamiento y validación
- `export_seed()` — escritura de archivo y path traversal

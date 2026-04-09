# Compliance — Requisitos del subject vs implementación actual

Análisis de cumplimiento de cada requisito del subject (v2.1) contra el código de la rama actual.

## Leyenda
- ✅ Cumplido
- ⚠️ Parcialmente cumplido / con matices
- ❌ No cumplido o con problema conocido

---

## Parte obligatoria

### Uso y manejo de errores

| Requisito | Estado | Notas |
|-----------|--------|-------|
| Nombre del archivo principal `a_maze_ing.py` | ✅ | Correcto |
| Un único argumento (config file) | ✅ | `sys.argv[1]` |
| Manejo elegante de todos los errores | ✅ | `try/except` global en `ft_make_maze()`, errores con mensaje de color |
| Nunca crashear inesperadamente | ✅ | `sys.exit(1)` en todos los puntos de error |

### Formato del archivo de configuración

| Requisito | Estado | Notas |
|-----------|--------|-------|
| Formato `CLAVE=VALOR` por línea | ✅ | Implementado en `ft_parsing_config()` |
| Líneas con `#` ignoradas | ⚠️ | Las líneas sin `=` se ignoran, pero el parser no verifica explícitamente `#`. Funciona en la práctica porque `#comment` no tiene `=` |
| `WIDTH` obligatorio | ✅ | |
| `HEIGHT` obligatorio | ✅ | |
| `ENTRY` obligatorio | ✅ | |
| `EXIT` obligatorio | ✅ | |
| `OUTPUT_FILE` obligatorio | ✅ | |
| `PERFECT` obligatorio | ✅ | |
| Claves adicionales permitidas | ✅ | `SEED`, `SEED_CODE`, `PRINT_MODE` añadidos |
| Config file por defecto en el repo | ✅ | `config.txt` en la raíz |

### Requisitos del laberinto

| Requisito | Estado | Notas |
|-----------|--------|-------|
| Generación aleatoria | ✅ | `random` con shuffle en DFS, `randrange` en Prim |
| Reproducibilidad mediante semilla | ✅ | `random.seed(self.maze.seed_code)` en `perfect_maze()` |
| Cada celda tiene 0-4 paredes (N/E/S/W) | ✅ | `Cell.walls` dict con 4 direcciones |
| Entrada y salida existen, son diferentes, dentro de límites | ✅ | Validado en `ConfigModel.check_entry/check_exit` |
| Conectividad total (sin celdas aisladas excepto "42") | ✅ | DFS/Prim garantizan spanning tree; "42" pre-marcado como visitado |
| Paredes en bordes externos | ✅ | Las celdas se inicializan con todas las paredes a `True`; solo se eliminan las internas |
| Coherencia de paredes entre celdas vecinas | ✅ | `opposite_wall()` garantiza simetría al eliminar paredes |
| Sin zonas abiertas > 2 celdas de ancho | ✅ | `open_areas()` detecta y subdivide áreas 2×3 y 3×2 |
| Patrón "42" visible en representación visual | ✅ | `watermark()` marca celdas con todas las paredes cerradas |
| `PERFECT=True` → exactamente un camino | ✅ | DFS/Prim generan spanning tree (laberinto perfecto) |
| `PERFECT=False` → laberinto imperfecto | ✅ | `non_perfect_maze()` elimina paredes adicionales |
| Mensaje de error si "42" no cabe | ✅ | `has_necessary_dimensions()` + print en `watermark()` |

### Formato del archivo de salida

| Requisito | Estado | Notas |
|-----------|--------|-------|
| Un dígito hex por celda | ✅ | `generate_seed()` con `f"{cell_walls:X}"` |
| Bit 0 = Norte, Bit 1 = Este, Bit 2 = Sur, Bit 3 = Oeste | ✅ | Implementado en `generate_seed()` |
| Pared cerrada = bit 1, abierta = bit 0 | ✅ | |
| Celdas almacenadas fila por fila | ✅ | `export_seed()` itera por filas |
| Línea vacía separadora | ✅ | `fd.write("\n")` tras el grid |
| Coordenadas de entrada en línea separada | ✅ | |
| Coordenadas de salida en línea separada | ✅ | |
| Camino más corto (N/E/S/W) en línea separada | ✅ | BFS + `path_to_directions()` |
| Todas las líneas terminan con `\n` | ✅ | |

---

## Representación visual

| Requisito | Estado | Notas |
|-----------|--------|-------|
| Renderizado ASCII en terminal | ✅ | `MazePainter_ascii` |
| Renderizado gráfico con MLX | ✅ | `MazePainter_mlx` |
| Mostrar paredes claramente | ✅ | Caracteres Unicode de caja / píxeles |
| Mostrar entrada | ✅ | Verde en ambos renderers |
| Mostrar salida | ✅ | Rojo en ambos renderers |
| Mostrar camino solución | ✅ | Azul en ambos renderers |
| Re-generar nuevo laberinto | ✅ | Opción 1 en ambos renderers |
| Mostrar/Ocultar camino más corto | ✅ | Opción 2 en ambos renderers |
| Cambiar colores de paredes | ✅ | Opción 3 en ambos renderers |
| Colores específicos para patrón "42" (opcional) | ✅ | Opción 4 + teclas R/G/B |

### Interacciones adicionales implementadas (bonus)
- Opción 5: Re-generar con algoritmo Prim
- Opción 6: Animación de varios laberintos con colores distintos
- Teclas R/G/B: color específico para el patrón "42"
- Visualización de `seed_code` en el menú

---

## Reutilización de código

| Requisito | Estado | Notas |
|-----------|--------|-------|
| Generación como clase única en módulo independiente | ⚠️ | La lógica está en `Maze` + `BuiltMaze` en `src/model/maze.py`. No es una clase llamada `MazeGenerator` pero es importable |
| Documentación de instanciación con ejemplo | ⚠️ | Documentado en `README.md` pero no hay un ejemplo de uso standalone explícito |
| Documentación de parámetros personalizados | ✅ | README documenta WIDTH, HEIGHT, SEED_CODE |
| Acceso a la estructura generada | ✅ | `maze.grid_maze` accesible |
| Acceso a la solución | ✅ | `maze.build.solve_maze()` |
| Paquete `mazegen-*` en la raíz del repo | ✅ | `mazegen-0.1.2-py3-none-any.whl` y `mazegen-0.1.2.tar.gz` |
| Instalable con pip | ✅ | `pyproject.toml` configurado |
| Elementos para reconstruir el paquete | ✅ | `pyproject.toml` presente |
| Documentación en README.md principal | ⚠️ | Presente pero podría ser más explícita como guía de uso standalone |

---

## Reglas generales

| Requisito | Estado | Notas |
|-----------|--------|-------|
| Python 3.10+ | ✅ | `requires-python = ">=3.10"` en pyproject.toml |
| Estándar flake8 | ✅ | Configurado en Makefile |
| Type hints en funciones y variables | ✅ | Presente en todo el código |
| mypy sin errores | ⚠️ | Configurado, pero `Any` usado en algunos retornos de validators Pydantic |
| Docstrings PEP 257 | ✅ | Todas las funciones y clases documentadas |
| Context managers para archivos | ✅ | `with open(...)` en todo el código |
| Makefile con `install`, `run`, `debug`, `clean`, `lint` | ✅ | Presente |
| `lint-strict` (opcional) | ✅ | Presente |
| Tests con pytest | ✅ | `tests/` con pytest |
| `.gitignore` | ✅ | Presente |

---

## README

| Requisito | Estado | Notas |
|-----------|--------|-------|
| Primera línea en cursiva con logins | ✅ | `_This project has been created as part of the 42 curriculum by joflorid, agiron-d_` |
| Sección "Description" | ✅ | Presente |
| Sección "Instructions" | ✅ | Presente con múltiples métodos de instalación |
| Sección "Resources" | ✅ | Presente con links y mención de uso de IA |
| Estructura y formato del config file | ✅ | Tabla completa de parámetros |
| Algoritmo de generación elegido | ✅ | DFS y Prim documentados |
| Por qué se eligió el algoritmo | ✅ | Sección "Algorithm Selection" |
| Qué parte del código es reutilizable | ✅ | Mencionado |
| Roles del equipo | ✅ | Sección "Team Roles and Responsibilities" |
| Planificación y evolución | ✅ | Sección "Project Planning and Evolution" |
| Qué funcionó bien / qué mejorar | ✅ | Sección "Retrospective" |
| Herramientas utilizadas | ✅ | Sección "Tools Utilized" |

---

## Bonuses implementados

| Bonus | Estado |
|-------|--------|
| Múltiples algoritmos de generación (DFS + Prim) | ✅ |
| Animación durante la visualización | ✅ (`animate_colored_mazes()`) |
| Carga de laberinto desde semilla (SEED) | ✅ (extra, no en el subject) |
| SEED_CODE para reproducibilidad explícita | ✅ (extra, no en el subject) |

---

## Puntos de atención para la evaluación

1. **Comentarios con `#`**: el parser ignora líneas sin `=`, lo que funciona para `# comentario`, pero si una línea tiene `#` y también `=` (ej: `# WIDTH=10`), se procesaría incorrectamente. Verificar si el evaluador prueba este caso.

2. **Nombre de la clase generadora**: el subject sugiere `MazeGenerator` como nombre de clase. La implementación usa `Maze` + `BuiltMaze`. Funcionalmente equivalente pero el nombre difiere.

3. **`PERFECT=false` como string**: Pydantic puede interpretar `"false"` como `True`. Verificar el comportamiento real con el config actual.

4. **Coherencia de paredes en el output**: el subject menciona que se provee un script de validación. La función `validate_solution()` en `seed.py` implementa exactamente esta validación.

5. **Modificación en vivo durante evaluación**: el subject indica que puede pedirse una modificación menor del código. Conocer bien la estructura de `BuiltMaze` y los renderers es clave.

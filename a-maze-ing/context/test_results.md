# Resultados de ejecución de tests de aceptación

Archivo: `tests/test_acceptance.py`
Fecha de ejecución: 2026-04-02
Entorno: Python 3.13.5 / pytest 8.3.4 / macOS darwin

---

## Resumen

| Métrica | Valor |
|---------|-------|
| Total de tests | 47 |
| Pasados | 47 |
| Fallidos | 0 |
| Errores | 0 |
| Tiempo de ejecución | 0.72s |
| Resultado | ✅ PASS |

---

## Resultados por grupo

### TC-01 — Parser de configuración (11 tests)

| Test | Descripción | Resultado |
|------|-------------|-----------|
| test_tc0101_valid_config | Config válido completo → ConfigModel correcto | ✅ PASS |
| test_tc0102_comment_lines_ignored | Líneas con # se ignoran | ✅ PASS |
| test_tc0103_comment_with_equals_ignored | `# OUTPUT_FILE=malicious.txt` no sobreescribe | ✅ PASS |
| test_tc0104_whitespace_trimming | Espacios alrededor de clave y valor se eliminan | ✅ PASS |
| test_tc0105_print_mode_uppercase | PRINT_MODE en minúsculas → convertido a mayúsculas | ✅ PASS |
| test_tc0106_file_not_found | Archivo inexistente → [ERROR] + exit(1) | ✅ PASS |
| test_tc0107_invalid_width_type | WIDTH=invalid → [ERROR] + exit(1) | ✅ PASS |
| test_tc0108_invalid_entry_format | ENTRY=abc → exit(1) | ✅ PASS |
| test_tc0109_seed_code_empty_generates_random | SEED_CODE vacío → entero aleatorio 1-50000 | ✅ PASS |
| test_tc0110_no_seed_defaults_empty | Sin clave SEED → maze_seed == '' | ✅ PASS |
| test_tc0111_seed_value_parsed | SEED=output/seed1.txt → maze_seed correcto | ✅ PASS |

### TC-02 — Validación del modelo ConfigModel (7 tests)

| Test | Descripción | Resultado |
|------|-------------|-----------|
| test_tc0201_width_less_than_3 | WIDTH < 3 → ValidationError | ✅ PASS |
| test_tc0202_width_times_height_over_1000 | WIDTH×HEIGHT >= 1000 → exit(1) con mensaje recursión | ✅ PASS |
| test_tc0203_width_times_height_999_valid | WIDTH×HEIGHT = 999 → válido | ✅ PASS |
| test_tc0204_entry_out_of_bounds | ENTRY fuera de límites → error | ✅ PASS |
| test_tc0205_entry_equals_exit | ENTRY == EXIT → error | ✅ PASS |
| test_tc0206_invalid_print_mode | PRINT_MODE inválido → error | ✅ PASS |
| test_tc0207_perfect_false_string | PERFECT=false como string → maze_perfect es False | ✅ PASS |

### TC-03 — Generación del laberinto (9 tests)

| Test | Descripción | Resultado |
|------|-------------|-----------|
| test_tc0301_reproducibility_same_seed | Mismo seed_code → mismo generate_seed() | ✅ PASS |
| test_tc0302_different_seeds_different_mazes | Diferente seed_code → diferente laberinto | ✅ PASS |
| test_tc0303_full_connectivity | Todas las celdas no-42 son accesibles desde ENTRY | ✅ PASS |
| test_tc0304_wall_symmetry | Paredes simétricas entre celdas vecinas | ✅ PASS |
| test_tc0305_border_walls | Celdas del borde tienen paredes externas cerradas | ✅ PASS |
| test_tc0306_no_3x3_open_area | No existe ninguna zona abierta 3×3 | ✅ PASS |
| test_tc0307_perfect_maze_single_path | PERFECT=True → exactamente un camino (spanning tree) | ✅ PASS |
| test_tc0308_imperfect_maze_multiple_paths | PERFECT=False → más aristas que un spanning tree | ✅ PASS |
| test_tc0309_imperfect_still_connected | PERFECT=False → laberinto sigue conectado | ✅ PASS |

### TC-04 — Patrón "42" / Watermark (6 tests)

| Test | Descripción | Resultado |
|------|-------------|-----------|
| test_tc0401_watermark_present_large_maze | WIDTH>=9, HEIGHT>=7 → watermark presente | ✅ PASS |
| test_tc0402_watermark_cells_all_walls_closed | Celdas del watermark tienen todas las paredes cerradas | ✅ PASS |
| test_tc0403_watermark_centered | Watermark centrado en el laberinto | ✅ PASS |
| test_tc0404_watermark_omitted_small_maze | WIDTH<9 o HEIGHT<7 → watermark omitido, mensaje en consola | ✅ PASS |
| test_tc0405_entry_on_watermark_rejected | ENTRY en celda del watermark → check_valid_position False | ✅ PASS |
| test_tc0406_watermark_cells_not_reachable | Celdas del watermark no son accesibles por BFS | ✅ PASS |

### TC-05 — Codificación hexadecimal (6 tests)

| Test | Descripción | Resultado |
|------|-------------|-----------|
| test_tc0501_seed_structure | generate_seed produce WIDTH columnas por HEIGHT filas | ✅ PASS |
| test_tc0502_all_walls_closed_is_F | Todas las paredes cerradas → 'F' | ✅ PASS |
| test_tc0503_no_walls_is_0 | Sin paredes → '0' | ✅ PASS |
| test_tc0504_only_north_is_1 | Solo pared Norte → '1' | ✅ PASS |
| test_tc0505_only_east_is_2 | Solo pared Este → '2' | ✅ PASS |
| test_tc0506_south_and_west_is_C | Paredes Sur y Oeste → 'C' (4+8=12) | ✅ PASS |

### TC-06 — Solver BFS (3 tests)

| Test | Descripción | Resultado |
|------|-------------|-----------|
| test_tc0601_solution_found | Laberinto perfecto → solución no vacía | ✅ PASS |
| test_tc0602_solution_is_valid_path | La solución no atraviesa paredes | ✅ PASS |
| test_tc0603_path_to_directions | path_to_directions convierte celdas a direcciones | ✅ PASS |

### TC-10 — Casos límite (5 tests)

| Test | Descripción | Resultado |
|------|-------------|-----------|
| test_tc1001_minimum_valid_maze | Laberinto mínimo 3×3 → genera sin error | ✅ PASS |
| test_tc1002_minimum_watermark_maze | Laberinto 9×7 → watermark presente | ✅ PASS |
| test_tc1003_maximum_allowed_maze | WIDTH×HEIGHT=999 → genera sin RecursionError | ✅ PASS |
| test_tc1004_entry_exit_opposite_corners | ENTRY=(0,0), EXIT=(14,9) → solución válida | ✅ PASS |
| test_tc1005_entry_exit_same_row | ENTRY y EXIT en la misma fila → solución válida | ✅ PASS |

---

## Hallazgos durante la implementación de los tests

### Hallazgo 1 — Flujo de exit(1) para límite de recursión
El `sys.exit(1)` por `WIDTH×HEIGHT >= 1000` solo se dispara cuando se pasa por `ft_parsing_config()`, no al instanciar `ConfigModel` directamente. `ConfigModel` lanza `pydantic.ValidationError`. Ambos comportamientos son correctos pero distintos según el punto de entrada.

### Hallazgo 2 — EXIT no puede coincidir con celdas del patrón "42"
En un laberinto 15×10, el centro es `(7,5)`. Las coordenadas `(9,7)` caen dentro del patrón "42". El programa detecta esto correctamente en `check_valid_position()` y termina con `sys.exit(1)`. Esto confirma que el subject se cumple: EXIT no puede coincidir con ninguna celda del watermark.

---

## Cobertura de criterios de aceptación

| Grupo AC | Criterios cubiertos | Tests |
|----------|---------------------|-------|
| AC-02 Parser | AC-02.1 a AC-02.12 | TC-01 (11 tests) |
| AC-03 Validación | AC-03.1 a AC-03.7 | TC-02 (7 tests) |
| AC-04 Generación | AC-04.1 a AC-04.11 | TC-03 (9 tests) |
| AC-05 Watermark | AC-05.1 a AC-05.6 | TC-04 (6 tests) |
| AC-06 Hex output | AC-06.2 a AC-06.5, AC-06.9 | TC-05 (6 tests) |
| AC-06 Solver | AC-06.9 a AC-06.12 | TC-06 (3 tests) |
| AC-03/04/05 | Casos límite | TC-10 (5 tests) |

### Criterios de aceptación sin cobertura automatizada
Los siguientes criterios requieren tests de integración con sistema de archivos real o display, no cubiertos en esta suite:

- AC-06.1 — Archivo creado en `./output/`
- AC-06.6/7/8/10 — Estructura completa del archivo de salida
- AC-06.13 — Path traversal bloqueado
- AC-08 / AC-09 — Representación visual ASCII y MLX
- AC-10 — Instalación del paquete pip
- AC-11 — flake8 / mypy
- AC-12.4/5 — Permisos de archivo

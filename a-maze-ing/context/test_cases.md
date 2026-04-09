# Casos de prueba — A-Maze-ing

Casos de prueba derivados de los criterios de aceptación y la documentación técnica.
Organizados por módulo. Incluyen casos felices, casos límite y casos de error.

---

## TC-01 — Parser de configuración (`ft_parser_config.py`)

### TC-01-01: Config válido completo
```
Dado: archivo config con WIDTH=10, HEIGHT=8, ENTRY=1,1, EXIT=9,7,
      PERFECT=True, OUTPUT_FILE=maze.txt, PRINT_MODE=mlx
Cuando: se llama a ft_parsing_config(config_file)
Entonces: devuelve ConfigModel con maze_width=10, maze_height=8,
          maze_entry=(1,1), maze_exit=(9,7), maze_perfect=True,
          maze_print_mode="MLX"
AC: AC-02.1
```

### TC-01-02: Líneas con comentarios ignoradas
```
Dado: config con "# WIDTH=99\nWIDTH=10\nHEIGHT=8"
Cuando: se parsea
Entonces: maze_width=10 (no 99)
AC: AC-02.2
```

### TC-01-03: Línea con # y = (edge case)
```
Dado: config con "# OUTPUT_FILE=malicious.txt\nWIDTH=10\nHEIGHT=8"
Cuando: se parsea
Entonces: maze_output NO es "malicious.txt" (la línea con # se ignora)
AC: AC-02.2
Nota: caso de atención para la evaluación
```

### TC-01-04: Espacios alrededor de clave y valor
```
Dado: config con "  WIDTH  =  10  \n  HEIGHT  =  8  "
Cuando: se parsea
Entonces: maze_width=10, maze_height=8
AC: AC-02.4
```

### TC-01-05: PRINT_MODE en minúsculas
```
Dado: config con "PRINT_MODE=ascii"
Cuando: se parsea
Entonces: maze_print_mode="ASCII"
AC: AC-02.5
```

### TC-01-06: Archivo no encontrado
```
Dado: ruta "/nonexistent/config.txt"
Cuando: se llama a ft_parsing_config
Entonces: imprime "[ERROR]" en stdout, sys.exit(1)
AC: AC-02.6, AC-12.1, AC-12.2
```

### TC-01-07: WIDTH con valor no numérico
```
Dado: config con "WIDTH=invalid"
Cuando: se parsea
Entonces: imprime "[ERROR]", sys.exit(1)
AC: AC-02.7
```

### TC-01-08: ENTRY con formato inválido
```
Dado: config con "WIDTH=10\nHEIGHT=10\nENTRY=abc"
Cuando: se parsea
Entonces: sys.exit(1)
AC: AC-02.9
```

### TC-01-09: SEED_CODE vacío genera valor aleatorio
```
Dado: config con "SEED_CODE="
Cuando: se parsea dos veces
Entonces: maze_seed_code es un entero entre 1 y 50000 en ambas ejecuciones
          (pueden ser distintos entre sí)
AC: AC-02.11
```

### TC-01-10: Sin clave SEED, maze_seed es cadena vacía
```
Dado: config sin línea SEED
Cuando: se parsea
Entonces: maze_seed == ""
AC: AC-02.12
```

### TC-01-11: SEED con valor, maze_seed es la ruta
```
Dado: config con "SEED=output/seed1.txt"
Cuando: se parsea
Entonces: maze_seed == "output/seed1.txt"
AC: AC-02.12
```

---

## TC-02 — Validación del modelo (`config_model.py`)

### TC-02-01: WIDTH menor que 3
```
Dado: maze_width=2
Cuando: se instancia ConfigModel
Entonces: ValidationError, sys.exit(1)
AC: AC-03.1
```

### TC-02-02: WIDTH × HEIGHT >= 1000
```
Dado: maze_width=32, maze_height=32 (1024 celdas)
Cuando: se instancia ConfigModel
Entonces: ValidationError con mensaje de recursión, sys.exit(1)
AC: AC-03.3
```

### TC-02-03: WIDTH × HEIGHT = 999 (límite válido)
```
Dado: maze_width=27, maze_height=37 (999 celdas)
Cuando: se instancia ConfigModel
Entonces: ConfigModel creado sin error
AC: AC-03.3
```

### TC-02-04: ENTRY fuera de límites
```
Dado: maze_width=10, maze_height=10, maze_entry=(10, 0)
Cuando: se instancia ConfigModel
Entonces: ValidationError con "[ERROR] Entry values are incorrect"
AC: AC-03.4
```

### TC-02-05: EXIT igual a ENTRY
```
Dado: maze_entry=(0,0), maze_exit=(0,0)
Cuando: se instancia ConfigModel
Entonces: ValidationError con "[ERROR] Exit values cannot be the same"
AC: AC-03.6
```

### TC-02-06: PRINT_MODE inválido
```
Dado: maze_print_mode="CONSOLE"
Cuando: se instancia ConfigModel
Entonces: ValidationError con "[ERROR] PRINT_MODE value is incorrect"
AC: AC-03.7
```

### TC-02-07: PERFECT=false como string
```
Dado: config con "PERFECT=false"
Cuando: se parsea y se instancia ConfigModel
Entonces: maze_perfect es False (no True)
AC: AC-03.x
Nota: punto de atención — Pydantic puede interpretar "false" como True
      sin coerción explícita. Verificar comportamiento real.
```

---

## TC-03 — Generación del laberinto (`maze.py`)

### TC-03-01: Reproducibilidad con mismo SEED_CODE
```
Dado: dos instancias de Maze con mismo maze_config (mismo seed_code)
Cuando: se llama a perfect_maze() en ambas
Entonces: maze.generate_seed() devuelve exactamente el mismo resultado
AC: AC-04.1, AC-07.1
```

### TC-03-02: Diferente resultado con diferente SEED_CODE
```
Dado: dos instancias de Maze con seed_code=1 y seed_code=2
Cuando: se llama a perfect_maze() en ambas
Entonces: generate_seed() devuelve resultados distintos
AC: AC-04.2
```

### TC-03-03: Conectividad total del laberinto
```
Dado: Maze(config) con WIDTH=15, HEIGHT=10, PERFECT=True
Cuando: se llama a perfect_maze()
Entonces: BFS desde ENTRY alcanza todas las celdas no is_FORTY_TWO
AC: AC-04.3
```

### TC-03-04: Coherencia de paredes entre celdas vecinas
```
Dado: laberinto generado de cualquier tamaño
Cuando: se itera por todas las celdas
Entonces: para cada celda (x,y) con pared Este=False,
          la celda (x+1,y) tiene pared Oeste=False
          (y viceversa para todas las direcciones)
AC: AC-04.4
```

### TC-03-05: Paredes en bordes externos
```
Dado: laberinto generado WIDTH=10, HEIGHT=8
Cuando: se inspeccionan las celdas del borde
Entonces:
  - Fila 0: todas las celdas tienen walls["N"]=True
  - Fila HEIGHT-1: todas las celdas tienen walls["S"]=True
  - Columna 0: todas las celdas tienen walls["W"]=True
  - Columna WIDTH-1: todas las celdas tienen walls["E"]=True
AC: AC-04.5
```

### TC-03-06: Sin zonas abiertas 3×3
```
Dado: laberinto generado de cualquier tamaño
Cuando: se escanea el grid buscando áreas 3×3 completamente abiertas
Entonces: no se encuentra ninguna
AC: AC-04.6
```

### TC-03-07: Laberinto perfecto tiene exactamente un camino
```
Dado: Maze con PERFECT=True, WIDTH=15, HEIGHT=10
Cuando: se genera el laberinto
Entonces: BFS desde ENTRY encuentra exactamente un camino a EXIT
          (no hay ciclos: número de aristas = número de celdas - 1)
AC: AC-04.7
```

### TC-03-08: Laberinto imperfecto tiene múltiples caminos
```
Dado: Maze con PERFECT=False, WIDTH=15, HEIGHT=10
Cuando: se genera el laberinto
Entonces: existen al menos dos caminos distintos entre ENTRY y EXIT
AC: AC-04.8
```

### TC-03-09: Laberinto imperfecto sigue conectado
```
Dado: Maze con PERFECT=False
Cuando: se genera el laberinto
Entonces: BFS desde ENTRY alcanza todas las celdas no is_FORTY_TWO
AC: AC-04.9
```

---

## TC-04 — Patrón "42" (`maze.py::BuiltMaze.watermark`)

### TC-04-01: Watermark presente con dimensiones suficientes
```
Dado: Maze con WIDTH=15, HEIGHT=10
Cuando: se llama a watermark()
Entonces: existen celdas con is_FORTY_TWO=True en el grid
          devuelve True
AC: AC-05.1
```

### TC-04-02: Celdas del watermark tienen todas las paredes cerradas
```
Dado: laberinto generado con WIDTH=15, HEIGHT=10
Cuando: se inspeccionan las celdas con is_FORTY_TWO=True
Entonces: todas tienen walls = {N:True, S:True, E:True, W:True}
AC: AC-05.2
```

### TC-04-03: Watermark centrado
```
Dado: Maze con WIDTH=15, HEIGHT=11 (centro en x=7, y=5)
Cuando: se llama a watermark()
Entonces: las celdas marcadas corresponden a las posiciones relativas
          del patrón "42" centradas en (7, 5)
AC: AC-05.3
```

### TC-04-04: Watermark omitido con dimensiones insuficientes
```
Dado: Maze con WIDTH=8, HEIGHT=6 (< 9×7)
Cuando: se llama a watermark()
Entonces: devuelve False
          imprime mensaje de error en consola
          no hay celdas con is_FORTY_TWO=True
AC: AC-05.4
```

### TC-04-05: ENTRY en celda del watermark es rechazado
```
Dado: Maze con WIDTH=15, HEIGHT=10
      ENTRY en coordenadas que coinciden con el patrón "42"
Cuando: se llama a check_valid_position()
Entonces: devuelve False
          imprime "The coordinates cannot match the pattern '42'"
AC: AC-05.5
```

### TC-04-06: Celdas del watermark no son accesibles
```
Dado: laberinto generado con watermark
Cuando: BFS desde ENTRY
Entonces: ninguna celda con is_FORTY_TWO=True aparece en el camino
AC: AC-05.6
```

---

## TC-05 — Archivo de salida (`maze.py::export_seed`)

### TC-05-01: Estructura del archivo de salida
```
Dado: laberinto generado WIDTH=5, HEIGHT=3
Cuando: se llama a export_seed()
Entonces: el archivo contiene:
  - 3 líneas de 5 caracteres hex cada una
  - 1 línea vacía
  - 1 línea con coordenadas de entrada "x,y"
  - 1 línea con coordenadas de salida "x,y"
  - 1 línea con la cadena de solución
AC: AC-06.2, AC-06.6, AC-06.7, AC-06.8, AC-06.9
```

### TC-05-02: Codificación hex correcta — celda con todas las paredes
```
Dado: celda con walls = {N:True, E:True, S:True, W:True}
Cuando: se codifica en generate_seed()
Entonces: el carácter es "F" (1+2+4+8=15=0xF)
AC: AC-06.3, AC-06.4
```

### TC-05-03: Codificación hex correcta — celda sin paredes
```
Dado: celda con walls = {N:False, E:False, S:False, W:False}
Cuando: se codifica en generate_seed()
Entonces: el carácter es "0"
AC: AC-06.3, AC-06.5
```

### TC-05-04: Codificación hex correcta — solo pared Norte
```
Dado: celda con walls = {N:True, E:False, S:False, W:False}
Cuando: se codifica
Entonces: el carácter es "1" (bit 0 = Norte)
AC: AC-06.3
```

### TC-05-05: Codificación hex correcta — solo pared Este
```
Dado: celda con walls = {N:False, E:True, S:False, W:False}
Cuando: se codifica
Entonces: el carácter es "2" (bit 1 = Este)
AC: AC-06.3
```

### TC-05-06: Codificación hex correcta — paredes Sur y Oeste
```
Dado: celda con walls = {N:False, E:False, S:True, W:True}
Cuando: se codifica
Entonces: el carácter es "C" (4+8=12=0xC)
AC: AC-06.3
```

### TC-05-07: Todas las líneas terminan con \n
```
Dado: archivo de salida generado
Cuando: se lee byte a byte
Entonces: cada línea termina con el carácter \n (0x0A)
AC: AC-06.10
```

### TC-05-08: La solución es el camino más corto
```
Dado: laberinto generado con solución conocida
Cuando: se compara la longitud de la solución BFS con otras rutas posibles
Entonces: no existe ninguna ruta más corta entre ENTRY y EXIT
AC: AC-06.11
```

### TC-05-09: La solución es válida (no atraviesa paredes)
```
Dado: archivo de salida con solución "SSEEN..."
Cuando: se sigue la solución celda a celda desde ENTRY
Entonces: cada movimiento corresponde a una pared abierta en esa dirección
          y se llega a EXIT al final
AC: AC-06.12
```

### TC-05-10: Path traversal bloqueado
```
Dado: OUTPUT_FILE="../malicious.txt"
Cuando: se llama a export_seed()
Entonces: PermissionError capturado, imprime "[ERROR]", sys.exit(1)
AC: AC-06.13
```

### TC-05-11: Directorio output creado automáticamente
```
Dado: directorio ./output/ no existe
Cuando: se llama a export_seed()
Entonces: el directorio ./output/ se crea y el archivo se escribe correctamente
AC: AC-06.1
```

---

## TC-06 — Solver BFS (`maze.py::BuiltMaze.get_cells_solve_maze`)

### TC-06-01: Solución encontrada en laberinto perfecto
```
Dado: laberinto perfecto generado
Cuando: se llama a solve_maze(entry, exit)
Entonces: devuelve una cadena no vacía de caracteres N/E/S/W
AC: AC-06.9
```

### TC-06-02: Solución es el camino más corto
```
Dado: laberinto 3×3 con estructura conocida
Cuando: se llama a solve_maze()
Entonces: la longitud de la solución es la mínima posible
AC: AC-06.11
```

### TC-06-03: Conversión de path a direcciones
```
Dado: path = [Cell(0,0), Cell(1,0), Cell(1,1)]
Cuando: se llama a path_to_directions(path)
Entonces: devuelve "ES" (Este luego Sur)
AC: AC-06.9
```

### TC-06-04: Sin solución devuelve cadena vacía
```
Dado: laberinto donde ENTRY y EXIT están desconectados (caso artificial)
Cuando: se llama a solve_maze()
Entonces: devuelve "" e imprime mensaje de error
AC: AC-06.9
```

---

## TC-07 — Carga desde semilla (`seed.py`)

### TC-07-01: Semilla válida carga el laberinto correctamente
```
Dado: archivo de semilla generado por el propio programa
Cuando: se llama a create_grid_from_seed()
Entonces: grid_seed contiene las celdas con las paredes correctas
          is_start y is_exit marcados correctamente
AC: AC-07.3
```

### TC-07-02: Semilla con paredes inconsistentes es rechazada
```
Dado: archivo de semilla donde celda (0,0) tiene pared Este=True
      pero celda (1,0) tiene pared Oeste=False
Cuando: se llama a validate_solution()
Entonces: devuelve False, imprime "[ERROR]", sys.exit(1)
AC: AC-07.4
```

### TC-07-03: Semilla con carácter hex inválido es rechazada
```
Dado: archivo de semilla con carácter "G" (no es hex válido)
Cuando: se llama a create_grid_from_seed()
Entonces: imprime "[ERROR] Invalid hex character", sys.exit(1)
AC: AC-07.5
```

### TC-07-04: Semilla con metadatos faltantes
```
Dado: archivo de semilla sin las líneas de entry/exit/solución
Cuando: se llama a get_seed_info()
Entonces: imprime mensaje de error sobre metadatos faltantes
AC: AC-07.4
```

### TC-07-05: Celdas con todas las paredes cerradas marcadas como FORTY_TWO
```
Dado: semilla con una celda codificada como "F" (todas las paredes)
Cuando: se carga la semilla
Entonces: esa celda tiene is_FORTY_TWO=True
AC: AC-05.2
```

---

## TC-08 — Flujo principal (`a_maze_ing.py`)

### TC-08-01: Flujo completo modo ASCII
```
Dado: config válido con PRINT_MODE=ascii, SEED=""
Cuando: se llama a ft_make_maze()
Entonces: se parsea config, se genera Maze, se llama a perfect_maze(),
          se llama a solve_maze(), se exporta el archivo,
          se instancia MazePainter_ascii y se llama a start_visual()
AC: AC-01.1
```

### TC-08-02: Flujo completo modo MLX
```
Dado: config válido con PRINT_MODE=mlx, SEED=""
Cuando: se llama a ft_make_maze()
Entonces: se instancia MazePainter_mlx y se llama a start_visual()
AC: AC-01.1
```

### TC-08-03: Flujo con semilla
```
Dado: config con SEED="output/maze.txt" (archivo existente)
Cuando: se llama a ft_make_maze()
Entonces: se instancia Seed, se llama a create_grid_from_seed()
          NO se instancia Maze ni se llama a perfect_maze()
AC: AC-07.3
```

### TC-08-04: Sin argumentos
```
Dado: sys.argv = ['a_maze_ing.py']
Cuando: se ejecuta el programa
Entonces: imprime "[ERROR] config file not specified", sys.exit(1)
AC: AC-01.2
```

### TC-08-05: Excepción inesperada capturada
```
Dado: ft_parsing_config lanza una excepción no esperada
Cuando: se ejecuta ft_make_maze()
Entonces: el except general captura la excepción, imprime "[ERROR]", sys.exit(1)
          el programa NO crashea
AC: AC-12.6
```

---

## TC-09 — Calidad del código

### TC-09-01: flake8 sin errores
```
Dado: el código fuente completo
Cuando: se ejecuta "flake8 ."
Entonces: salida vacía, código de retorno 0
AC: AC-11.1
```

### TC-09-02: mypy sin errores
```
Dado: el código fuente completo
Cuando: se ejecuta mypy con los flags del subject
Entonces: "Success: no issues found", código de retorno 0
AC: AC-11.2
```

---

## TC-10 — Casos límite del laberinto

### TC-10-01: Laberinto mínimo válido (3×3)
```
Dado: WIDTH=3, HEIGHT=3, ENTRY=0,0, EXIT=2,2
Cuando: se genera el laberinto
Entonces: se genera sin error (sin watermark, con mensaje de consola)
          el archivo de salida tiene 3 líneas de 3 caracteres hex
AC: AC-03.1, AC-05.4
```

### TC-10-02: Laberinto mínimo con watermark (9×7)
```
Dado: WIDTH=9, HEIGHT=7, ENTRY=0,0, EXIT=8,6
Cuando: se genera el laberinto
Entonces: watermark() devuelve True
          existen celdas con is_FORTY_TWO=True
AC: AC-05.1
```

### TC-10-03: Laberinto máximo permitido (WIDTH×HEIGHT=999)
```
Dado: WIDTH=27, HEIGHT=37
Cuando: se genera el laberinto
Entonces: se genera sin RecursionError
          el archivo de salida tiene 37 líneas de 27 caracteres hex
AC: AC-03.3
```

### TC-10-04: ENTRY en esquina (0,0), EXIT en esquina opuesta
```
Dado: WIDTH=15, HEIGHT=10, ENTRY=0,0, EXIT=14,9
Cuando: se genera y resuelve el laberinto
Entonces: la solución existe y es válida
AC: AC-06.11, AC-06.12
```

### TC-10-05: ENTRY y EXIT en el mismo borde
```
Dado: WIDTH=15, HEIGHT=10, ENTRY=0,0, EXIT=14,0
Cuando: se genera y resuelve el laberinto
Entonces: la solución existe y es válida
AC: AC-06.11
```

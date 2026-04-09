# Criterios de aceptación — A-Maze-ing

Criterios derivados del subject v2.1 y la documentación técnica del proyecto.
Cada criterio está vinculado a un requisito del subject y es verificable de forma objetiva.

---

## AC-01 — Ejecución del programa

**Requisito:** El programa debe ejecutarse con `python3 a_maze_ing.py config.txt`

| ID | Criterio |
|----|----------|
| AC-01.1 | El programa acepta exactamente un argumento (ruta al config file) |
| AC-01.2 | Si no se pasa ningún argumento, imprime un mensaje de error con `[ERROR]` y termina con código 1 |
| AC-01.3 | Si se pasan más de un argumento, imprime un mensaje de error y termina con código 1 |
| AC-01.4 | El archivo principal se llama `a_maze_ing.py` |

---

## AC-02 — Parsing del archivo de configuración

**Requisito:** Formato `CLAVE=VALOR`, líneas con `#` ignoradas, claves obligatorias presentes

| ID | Criterio |
|----|----------|
| AC-02.1 | Un config válido con todas las claves obligatorias produce un `ConfigModel` sin errores |
| AC-02.2 | Las líneas que empiezan con `#` se ignoran completamente |
| AC-02.3 | Las líneas sin `=` se ignoran sin error |
| AC-02.4 | Los espacios alrededor de clave y valor se eliminan (`  WIDTH  =  10  ` → `maze_width=10`) |
| AC-02.5 | `PRINT_MODE` se convierte a mayúsculas independientemente de cómo se escriba |
| AC-02.6 | Si el archivo de config no existe, imprime `[ERROR]` y termina con código 1 |
| AC-02.7 | Si `WIDTH` no es un entero válido, imprime `[ERROR]` y termina con código 1 |
| AC-02.8 | Si `HEIGHT` no es un entero válido, imprime `[ERROR]` y termina con código 1 |
| AC-02.9 | Si `ENTRY` no tiene formato `x,y` con enteros, imprime `[ERROR]` y termina con código 1 |
| AC-02.10 | Si `EXIT` no tiene formato `x,y` con enteros, imprime `[ERROR]` y termina con código 1 |
| AC-02.11 | Si `SEED_CODE` está vacío o ausente, se genera un valor aleatorio entre 1 y 50000 |
| AC-02.12 | Si `SEED` está vacío o ausente, `maze_seed` toma el valor `""` |

---

## AC-03 — Validación del modelo de configuración

**Requisito:** Validaciones de negocio sobre los valores del config

| ID | Criterio |
|----|----------|
| AC-03.1 | `WIDTH` debe ser ≥ 3; si es menor, termina con código 1 |
| AC-03.2 | `HEIGHT` debe ser ≥ 3; si es menor, termina con código 1 |
| AC-03.3 | `WIDTH × HEIGHT` debe ser < 1000; si no, termina con código 1 con mensaje de recursión |
| AC-03.4 | Las coordenadas de `ENTRY` deben estar dentro de `[0, WIDTH-1] × [0, HEIGHT-1]` |
| AC-03.5 | Las coordenadas de `EXIT` deben estar dentro de `[0, WIDTH-1] × [0, HEIGHT-1]` |
| AC-03.6 | `ENTRY` y `EXIT` no pueden ser iguales |
| AC-03.7 | `PRINT_MODE` debe ser `ASCII` o `MLX` (insensible a mayúsculas); cualquier otro valor termina con código 1 |
| AC-03.8 | `OUTPUT_FILE` debe tener al menos 5 caracteres |

---

## AC-04 — Generación del laberinto

**Requisito:** Laberinto aleatorio, reproducible, válido, sin zonas abiertas > 2 celdas

| ID | Criterio |
|----|----------|
| AC-04.1 | Dos ejecuciones con el mismo `SEED_CODE` producen exactamente el mismo laberinto |
| AC-04.2 | Dos ejecuciones con diferente `SEED_CODE` producen laberintos distintos (con alta probabilidad) |
| AC-04.3 | Todas las celdas del laberinto son accesibles desde la entrada (conectividad total), excepto las celdas del patrón "42" |
| AC-04.4 | Las paredes de celdas vecinas son simétricas: si la celda A tiene pared Este, la celda B adyacente tiene pared Oeste |
| AC-04.5 | Las celdas del borde exterior tienen paredes en los lados que dan al exterior |
| AC-04.6 | No existe ninguna zona abierta de 3×3 o mayor en el laberinto generado |
| AC-04.7 | Con `PERFECT=True`, existe exactamente un camino entre `ENTRY` y `EXIT` |
| AC-04.8 | Con `PERFECT=False`, pueden existir múltiples caminos entre `ENTRY` y `EXIT` |
| AC-04.9 | Con `PERFECT=False`, el laberinto sigue siendo completamente conectado |
| AC-04.10 | El laberinto se genera con el algoritmo DFS por defecto |
| AC-04.11 | El laberinto puede generarse con el algoritmo Prim como alternativa |

---

## AC-05 — Patrón "42"

**Requisito:** Patrón visible de celdas completamente cerradas; omitido si el laberinto es demasiado pequeño

| ID | Criterio |
|----|----------|
| AC-05.1 | Con `WIDTH ≥ 9` y `HEIGHT ≥ 7`, el laberinto contiene celdas marcadas como `is_FORTY_TWO=True` formando el patrón "42" |
| AC-05.2 | Las celdas del patrón "42" tienen todas sus paredes cerradas (`walls = {N:True, S:True, E:True, W:True}`) |
| AC-05.3 | El patrón "42" se posiciona en el centro del laberinto |
| AC-05.4 | Con `WIDTH < 9` o `HEIGHT < 7`, se imprime un mensaje de error en consola y el patrón se omite |
| AC-05.5 | `ENTRY` y `EXIT` no pueden coincidir con celdas del patrón "42"; si coinciden, el programa termina con error |
| AC-05.6 | Las celdas del patrón "42" no son accesibles desde el resto del laberinto (están aisladas) |

---

## AC-06 — Archivo de salida

**Requisito:** Formato hex, fila por fila, línea vacía, entry, exit, solución

| ID | Criterio |
|----|----------|
| AC-06.1 | El archivo de salida se crea en `./output/<OUTPUT_FILE>` |
| AC-06.2 | Cada fila del laberinto ocupa exactamente una línea, con `WIDTH` caracteres hex |
| AC-06.3 | Cada carácter hex codifica correctamente las paredes: bit 0=N, bit 1=E, bit 2=S, bit 3=W |
| AC-06.4 | Una celda con todas las paredes cerradas se codifica como `F` |
| AC-06.5 | Una celda sin paredes se codifica como `0` |
| AC-06.6 | Tras las filas del laberinto hay exactamente una línea vacía |
| AC-06.7 | La línea siguiente a la vacía contiene las coordenadas de entrada en formato `x,y` |
| AC-06.8 | La línea siguiente contiene las coordenadas de salida en formato `x,y` |
| AC-06.9 | La última línea contiene el camino más corto como cadena de caracteres `N`, `E`, `S`, `W` |
| AC-06.10 | Todas las líneas del archivo terminan con `\n` |
| AC-06.11 | El camino de la solución es el más corto posible (BFS garantiza optimalidad) |
| AC-06.12 | Siguiendo el camino de la solución desde `ENTRY`, se llega a `EXIT` sin atravesar paredes |
| AC-06.13 | No se puede escribir fuera del directorio `./output/` (path traversal bloqueado) |

---

## AC-07 — Reproducibilidad mediante semilla

**Requisito:** El laberinto debe ser reproducible con la misma semilla

| ID | Criterio |
|----|----------|
| AC-07.1 | Con el mismo `SEED_CODE`, el archivo de salida es idéntico byte a byte en dos ejecuciones |
| AC-07.2 | El `SEED_CODE` se muestra en la interfaz visual para que el usuario pueda anotarlo |
| AC-07.3 | Con `SEED=<ruta>`, el programa carga el laberinto desde el archivo de semilla en lugar de generar uno nuevo |
| AC-07.4 | Un archivo de semilla con paredes inconsistentes entre celdas vecinas es rechazado con error |
| AC-07.5 | Un archivo de semilla con formato hex inválido es rechazado con error |

---

## AC-08 — Representación visual ASCII

**Requisito:** Renderizado en terminal con paredes, entrada, salida y solución visibles

| ID | Criterio |
|----|----------|
| AC-08.1 | El laberinto se renderiza con caracteres de caja Unicode (`┌ ─ ┬ │ ┼ └`) |
| AC-08.2 | La celda de entrada se muestra con un color distinto (verde) |
| AC-08.3 | La celda de salida se muestra con un color distinto (rojo) |
| AC-08.4 | Las celdas del patrón "42" se muestran con un carácter de relleno (`███`) |
| AC-08.5 | El camino solución se muestra en azul cuando está activado |
| AC-08.6 | El menú muestra la opción de re-generar el laberinto (opción 1) |
| AC-08.7 | El menú muestra la opción de mostrar/ocultar el camino (opción 2) |
| AC-08.8 | El menú muestra la opción de cambiar el color de las paredes (opción 3) |
| AC-08.9 | Una selección inválida en el menú muestra un mensaje de error y vuelve a pedir input |
| AC-08.10 | La opción de salir termina el programa limpiamente |

---

## AC-09 — Representación visual MLX

**Requisito:** Renderizado gráfico con las mismas funcionalidades que ASCII

| ID | Criterio |
|----|----------|
| AC-09.1 | Se abre una ventana gráfica con el laberinto renderizado píxel a píxel |
| AC-09.2 | La celda de entrada se muestra en verde |
| AC-09.3 | La celda de salida se muestra en rojo |
| AC-09.4 | Las celdas del patrón "42" se muestran en blanco por defecto |
| AC-09.5 | El camino solución se muestra en azul cuando está activado |
| AC-09.6 | La tecla `1` re-genera el laberinto con DFS |
| AC-09.7 | La tecla `2` alterna mostrar/ocultar el camino solución |
| AC-09.8 | La tecla `3` cambia el color de las paredes aleatoriamente |
| AC-09.9 | La tecla `4` cambia el color del patrón "42" aleatoriamente |
| AC-09.10 | La tecla `5` re-genera el laberinto con Prim |
| AC-09.11 | La tecla `7` o ESC cierra la ventana y termina el programa |
| AC-09.12 | Cerrar la ventana con el botón X termina el programa limpiamente |
| AC-09.13 | El menú en pantalla muestra el `seed_code` actual |

---

## AC-10 — Reutilización del módulo

**Requisito:** Módulo instalable con pip, documentado, con acceso a estructura y solución

| ID | Criterio |
|----|----------|
| AC-10.1 | El paquete `mazegen-*.whl` o `mazegen-*.tar.gz` existe en la raíz del repositorio |
| AC-10.2 | El paquete se puede instalar con `pip install mazegen-*.whl` en un virtualenv limpio |
| AC-10.3 | Tras la instalación, `from src.model.maze import Maze` funciona sin errores |
| AC-10.4 | Se puede instanciar `Maze(config)` y llamar a `build.perfect_maze()` sin importar el resto del proyecto |
| AC-10.5 | `maze.build.solve_maze(entry, exit)` devuelve una cadena de direcciones válida |
| AC-10.6 | `maze.grid_maze` es accesible y contiene la estructura de celdas |
| AC-10.7 | El paquete se puede reconstruir desde `pyproject.toml` con `python -m build` |

---

## AC-11 — Calidad del código

**Requisito:** Python 3.10+, flake8, mypy, docstrings, type hints

| ID | Criterio |
|----|----------|
| AC-11.1 | `make lint` ejecuta sin errores de flake8 |
| AC-11.2 | `make lint` ejecuta mypy sin errores con los flags del subject |
| AC-11.3 | Todas las funciones públicas tienen docstrings |
| AC-11.4 | Todas las funciones tienen type hints en parámetros y retorno |
| AC-11.5 | Todos los archivos usan context managers (`with`) para apertura de archivos |
| AC-11.6 | No hay excepciones no capturadas que puedan crashear el programa |

---

## AC-12 — Manejo de errores

**Requisito:** El programa nunca crashea; siempre muestra mensajes de error claros

| ID | Criterio |
|----|----------|
| AC-12.1 | Cualquier error produce un mensaje que contiene `[ERROR]` |
| AC-12.2 | El programa termina con código de salida 1 en cualquier error |
| AC-12.3 | El programa termina con código de salida 0 en ejecución normal |
| AC-12.4 | Un archivo de config con permisos de lectura denegados produce `[ERROR]` y código 1 |
| AC-12.5 | Un directorio de salida sin permisos de escritura produce `[ERROR]` y código 1 |
| AC-12.6 | Coordenadas de `ENTRY` o `EXIT` fuera de los límites producen `[ERROR]` y código 1 |
| AC-12.7 | `ENTRY` igual a `EXIT` produce `[ERROR]` y código 1 |

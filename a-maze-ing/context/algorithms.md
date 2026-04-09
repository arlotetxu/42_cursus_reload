# Algoritmos

## Generación de laberintos

### DFS — Depth-First Search (por defecto)

Implementación recursiva con backtracking.

**Proceso:**
1. Marca la celda actual como visitada
2. Obtiene los vecinos no visitados y los mezcla aleatoriamente
3. Para cada vecino no visitado, elimina la pared entre ambas celdas y llama recursivamente
4. El backtracking ocurre de forma implícita al retornar de la recursión

**Características:**
- Genera laberintos con pasillos largos y sinuosos
- Tiende a producir un camino principal largo con pocas bifurcaciones
- Complejidad: O(n) donde n = número de celdas
- Limitación: profundidad de recursión máxima ≈ n → por eso `width × height < 1000`

```
dfs(celda_actual):
    celda_actual.visited = True
    vecinos = get_neighbors(celda_actual)  # solo no visitados
    shuffle(vecinos)
    para cada (vecino, pared) en vecinos:
        si no vecino.visited:
            eliminar pared entre celda_actual y vecino
            dfs(vecino)
```

---

### Prim — Algoritmo de Prim

Implementación iterativa basada en una lista de frontera.

**Proceso:**
1. Marca la celda inicial como visitada
2. Añade sus vecinos a la lista de frontera
3. Mientras haya frontera: selecciona un candidato aleatorio, lo conecta con su origen eliminando la pared, y añade sus nuevos vecinos a la frontera

**Características:**
- Genera laberintos más "ramificados" y uniformes
- No tiene límite de recursión (iterativo)
- Produce texturas visuales distintas al DFS

```
prim(celda_inicial):
    celda_inicial.visited = True
    frontera = [(vecino, origen, pared) para vecino en vecinos(celda_inicial)]
    mientras frontera no vacía:
        (candidato, origen, pared) = frontera.pop(índice_aleatorio)
        si candidato.visited: continuar
        candidato.visited = True
        eliminar pared entre origen y candidato
        añadir vecinos de candidato a frontera
```

---

### Laberinto imperfecto (`PERFECT=false`)

Tras generar el laberinto perfecto, se eliminan paredes adicionales para crear ciclos:

- Se calcula `walls_to_remove = int(width × height × 0.2)` (20% de celdas)
- Para cada eliminación: se elige una celda aleatoria y se elimina una pared aleatoria hacia un vecino válido (no `is_FORTY_TWO`)

---

### Eliminación de zonas abiertas — `open_areas()`

Tras la generación, se detectan y subdividen áreas rectangulares completamente abiertas (2×3 o 3×2 celdas sin paredes internas):

- Se escanea el grid en múltiples pasadas (máximo 10)
- Por cada área detectada se añade una pared con un hueco aleatorio
- El proceso termina cuando no se encuentran más áreas abiertas o se alcanza el límite de pasadas

---

## Resolución — BFS (Breadth-First Search)

Encuentra el camino más corto entre entrada y salida.

**Proceso:**
1. Resetea el estado `visited` de todas las celdas (excepto `is_FORTY_TWO`)
2. Explora en anchura usando una lista como cola
3. Mantiene un diccionario `parent` para reconstruir el camino
4. Al llegar a la celda de salida, reconstruye el path hacia atrás

```
bfs(start, exit):
    cola = [start]
    start.visited = True
    parent = {}
    mientras cola no vacía:
        celda = cola.pop(0)
        si celda == exit:
            reconstruir camino desde parent
            return camino
        para cada dirección abierta en celda:
            vecino = celda en esa dirección
            si vecino no visitado y no is_FORTY_TWO:
                vecino.visited = True
                parent[vecino] = celda
                cola.append(vecino)
    return None  # sin solución
```

**Conversión a direcciones:**
El camino (lista de celdas) se convierte a una cadena de caracteres `N/S/E/W` comparando las coordenadas de celdas consecutivas.

---

## Watermark "42"

El patrón "42" se dibuja en el centro del laberinto marcando celdas como `is_FORTY_TWO = True` y `visited = True` antes de la generación.

- Requiere `width ≥ 9` y `height ≥ 7`
- Las celdas marcadas no participan en la generación (no se eliminan sus paredes)
- El algoritmo de generación las rodea naturalmente
- La validación impide que `ENTRY` o `EXIT` coincidan con estas celdas

**Posiciones relativas al centro del laberinto:**

```
Dígito "4":          Dígito "2":
(-3,-2) (-1,-2)      (1,-2)(2,-2)(3,-2)
(-3,-1) (-1,-1)               (3,-1)
(-3, 0)(-2, 0)(-1, 0)  (1, 0)(2, 0)(3, 0)
        (-1, 1)      (1, 1)
        (-1, 2)      (1, 2)(2, 2)(3, 2)
```

---

## Validación de semilla

Antes de cargar un archivo de semilla, `validate_solution()` verifica la consistencia de las paredes entre celdas adyacentes:

Para cada celda `(c, r)` con valor hex `v`:
- Norte: `v & 1 == (grid[r-1][c] >> 2) & 1`
- Este: `(v >> 1) & 1 == (grid[r][c+1] >> 3) & 1`
- Sur: `(v >> 2) & 1 == grid[r+1][c] & 1`
- Oeste: `(v >> 3) & 1 == (grid[r][c-1] >> 1) & 1`

Si alguna condición falla, el archivo se considera inválido y el programa termina con error.

"""
Escribe una función que represente una constelación de estrellas sobre una
cuadrícula y devuelva su representación visual como una lista de cadenas.

Declaración:
def constellation_mapper(stars: list[tuple[int, int]], size:int) -> list[str]:

La función debe:
- Recibir una lista de coordenadas de estrellas en forma de tuplas (fila, columna)
y el tamaño de la cuadrícula como un entero
- Devolver una lista de cadenas que represente la cuadrícula
- La estrellas se representan con '*' y los espacios vacíos con '.'
- Las coordenadas de la cuadrícula comienzan en (0,0) en la esquina superior
izquierda
- Ignorar las coordenadas que estén fuera de los límites de la cuadrícula
- Manejar coordenadas duplicadas (La estrella solo aparece una vez)

Ejemplos:
([(0,0), (1,1), (2,2)], 3) -> ['*..', '.*.', '..*']
([(1,1), (0,1), (2,1), (1,0), (1,2)], 3) -> ['.*.', '***', '.*.']
([], 2) -> ['..', '..']
([(0,0), (0,0), (1,1)], 2) -> ['*.', '.*']
([(0,0), (5,5)], 3) -> ['*..', '...', '...']
([(1,0), (1,1), (1,2)], 3) -> ['...', '***', '...']
"""

def constellation_mapper(stars: list[tuple[int, int]], size:int) -> list[str]:
    res = [[0 for _ in range(0, size)] for _ in range(0, size)]
    for tup in stars:
        y, x = tup
        try:
            res[y][x] = 1
        except Exception:
            continue
    
    ret = []
    for list_ in res:
        cad = ""
        for item in list_:
            if item == 1:
                cad += '*'
            else:
                cad += '.'
        ret.append(cad)

    return ret

print(constellation_mapper([(0,0), (1,1), (2,2)], 3))
print(constellation_mapper([(1,1), (0,1), (2,1), (1,0), (1,2)], 3))
print(constellation_mapper([], 2))
print(constellation_mapper([(0,0), (0,0), (1,1)], 2))
print(constellation_mapper([(0,0), (5,5)], 3))
print(constellation_mapper([(1,0), (1,1), (1,2)], 3))
"""
Escribe una función que combine multiples listas ordenadas en una unica lista
ordenada, manteniendo el orden de forma eficiente.

Declaración:
def merge_sorted_list(lists: list[list[int]]) -> list[int]

La función debe:
- Recibir una lista de listas de enteros ordenados como entrada
- Devolver una unica lista combinada en orden ascendente
- Conservar todos los elementos duplicados en el resultado final
- Manejar correctamente listas vacias y entradas vacias
- Mantener una eficiencia optima para entradas de gran tamaño.

Reglas:
- Se garantiza que todas las listas de entrada estarán ordenadas de forma
ascendente
- Las listas vacias deben ignorarse durante la combinación.
- Devolver una lista vacia si no se proporciona ninguna entrada valida.
- Consevar duplicados entre diferentes listas
- Manejar correctamente los numeros negativos

Ejemplos:
[[1,3,5], [2,4,6]] -> [1,2,3,4,5,6]
[[1,5,9], [2,3,8], [4,6,7]] -> [1,2,3,4,5,6,7,8,9]
[[5], [1,3], [2,4]] -> [1,2,3,4,5]
[[1,1,2], [2,3,3]] -> [1,1,2,2,3,3]
[[], [1,2,3]] -> [1,2,3]
[] -> []
[[-5,-1,0], [-3,2,4]] -> [-5,-3,-1,0,2,4]
[[10], [10], [10]] -> [10,10,10]
"""

def merge_sorted_list(lists: list[list[int]]) -> list[int]:
    res = []
    for list_ in lists:
        for item in list_:
            res.append(item)
    res.sort()
    return res

print(merge_sorted_list([[1,3,5], [2,4,6]]))
print(merge_sorted_list([[1,5,9], [2,3,8], [4,6,7]]))
print(merge_sorted_list([[5], [1,3], [2,4]]))
print(merge_sorted_list([[1,1,2], [2,3,3]]))
print(merge_sorted_list([[], [1,2,3]]))
print(merge_sorted_list([]))
print(merge_sorted_list([[-5,-1,0], [-3,2,4]]))
print(merge_sorted_list([[10], [10], [10]]))

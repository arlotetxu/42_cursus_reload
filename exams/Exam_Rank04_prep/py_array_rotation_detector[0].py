'''
Escibe una funcion que determine si un array es una rotación de otro array.
Una rotación significa que el array ha sido desplazado de forma circular hacia
la izquierda o hacia la derecha.

Tu función debe declararse:
def array_rotation_detector(arr1: list[int], arr2: list[int]) -> bool:

La función debe:
- Comprobar si arr2 es una rotación de arr1
- Manejar arrays de diferentes longitudes (debe devolver False)
- Manejar arrays vacíos (dos arrays vacíos son rotaciones)
- Tener en cuenta que una rotación puede ser de 0 posiciones (mismo array)
- Considerar rotaciones tanto a la derecha como a la izquierda.

Ejemplos:
[1,2,3,4,5] [3,4,5,1,2] -> True
[1,2,3,4,5] [4,5,1,2,3] -> True
[1,2,3,4,5] [1,2,3,4,5] -> True
[1,2,3,4,5] [2,3,4,5,1] -> True
[1,2,3] [1,3,2] -> False
[1,2,3] [1,2] -> False
[] [] -> True
[1,1,1] [1,1,1] -> True
'''

def array_rotation_detector(arr1: list[int], arr2: list[int]) -> bool:
    if len(arr1) != len(arr2):
        return False
    if arr1 == arr2:
        return True
    #Rotamos a la derecha
    for i in range(0, len(arr1)):
        num = arr1.pop(0)
        arr1.append(num)
        if arr1 == arr2:
            return True
    
    #Rotamos a la izquierda
    for i in range(0, len(arr1)):
        num = arr1.pop(len(arr1) - 1)
        arr1.insert(0, num)
        if arr1 == arr2:
            return True
    return False

print(array_rotation_detector([1,2,3,4,5], [3,4,5,1,2]))
print(array_rotation_detector([1,2,3,4,5], [4,5,1,2,3]))
print(array_rotation_detector([1,2,3,4,5], [1,2,3,4,5]))
print(array_rotation_detector([1,2,3,4,5], [2,3,4,5,1]))
print(array_rotation_detector([1,2,3], [1,3,2]))
print(array_rotation_detector([1,2,3], [1,2]))
print(array_rotation_detector([], []))
print(array_rotation_detector([1,1,1], [1,1,1]))
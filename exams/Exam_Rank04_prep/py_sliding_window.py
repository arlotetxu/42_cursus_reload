"""
Sacar los valores maximos de cada grupo de 3 elementos de una lista, iterando
de uno en uno
"""

def sliding_window(lst: list[int]) -> list[int]:
    res = []
    for i in range(0, len(lst)-2):
        res.append(max(lst[i:i+3]))
    print(res)


sliding_window([3,4,15,7,8,9,12,13,14])
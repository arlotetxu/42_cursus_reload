"""
Sacar los elementos comunes de listas. No se si el argumento es una lista de
listas o listas independientes
"""

def common_list(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []
    return list(set(lists[0]).intersection(*lists[1:]))


def common_list_2(lst1: list[int], lst2: list[int], lst3: list[int]) -> list[int]:
    return list(set(lst1) & set(lst2) & set(lst3))


print(common_list([[1,2,3,4], [3,4,5,6], [3,8,9]]))
print(common_list_2([1,2,3,4], [3,4,5,6], [3,8,9]))
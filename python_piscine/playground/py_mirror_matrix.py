def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    ret = []

    for item in matrix:
        rev = item[::-1]
        ret.append(rev)

    print(ret)
    return ret

mirror_matrix([[-1, -2], [-3, -4]])


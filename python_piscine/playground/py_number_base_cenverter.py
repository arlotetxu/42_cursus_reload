def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    template = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z']

    if from_base > 36 or from_base < 2 or to_base > 36 or to_base < 2:
        return "ERROR"
    for c in number:
        if c not in template[0: from_base]:
            return "ERROR"

    num_dec = int(number, base=from_base)
    inv_ret = ""
    while int(num_dec) > 0:
        inv_ret += template[int((num_dec % to_base))]
        num_dec /= to_base
    ret = inv_ret[::-1]
    return ret

number_base_converter("1010", 2, 10)
number_base_converter("FF", 16, 10)
number_base_converter("255", 10, 16)
number_base_converter("123", 10, 2)
number_base_converter("Z", 36, 10)
number_base_converter("35", 10, 36)
number_base_converter("123", 1, 10)
number_base_converter("G", 16, 10)

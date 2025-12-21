#!/usr/bin/env python3

import math
import sys

# FUNCTIONS==================================================================


def ft_argv_len(argv: list) -> int:
    argv_len = 0
    for arg in argv:
        argv_len += 1
    return argv_len


def coord_cast(coord_list: list) -> tuple:
    """
    Convert a list of coordinates to a tuple of integers.

    Args:
        # coord_list (list): A list of coordinate values that can be cast
            to integers.

    Returns:
        tuple: A tuple containing the coordinate values converted to integers.

    Example:
        >>> coord_cast(['1', '2', '3'])
        (1, 2, 3)
    """
    my_coord_tuple = tuple([int(item) for item in coord_list])
    return my_coord_tuple


def calc_distance(coord_0: tuple, coord_1: tuple) -> tuple[tuple, float]:
    """
    Calculate the Euclidean distance between two 3D coordinates.

    Args:
        coord_0 (tuple): The first coordinate point as a tuple (x, y, z).
        coord_1: The second coordinate point as a tuple (x, y, z).

    Returns:
        tuple: A tuple containing the second coordinate
        float: The calculated Euclidean distance between the two points.
    """
    diff_x = (coord_1[0] - coord_0[0]) ** 2
    diff_y = (coord_1[1] - coord_0[1]) ** 2
    diff_z = (coord_1[2] - coord_0[2]) ** 2

    distance = math.sqrt(diff_x + diff_y + diff_z)
    return coord_1, distance


# MAIN=======================================================================
if __name__ == "__main__":
    coord_0 = (0, 0, 0)
    print("=== Game Coordinate System ===")

    # Case 1 - Coordinates in a tuple
    my_init_coord = (10, 20, 5)
    print(f"\nPosition created: {my_init_coord}")
    final_coord, dist = calc_distance(coord_0, my_init_coord)
    print(f"Distance between {coord_0} and {my_init_coord}: {dist:.2f}")

    # Case 2 - Coordinates in a string
    my_str_coord = "3,4,0"
    my_int_list = my_str_coord.split(",")
    try:
        print(f'\nParsing coordinates: "{my_str_coord}"')
        my_int_coord = coord_cast(my_int_list)
        print(f"Parsed position: {my_int_coord}")
    except ValueError as e:
        print("❌ Upss... something went wrong while parsing coordinates 🤷")
        print(f"Error details - Type: {e.__class__.__name__}, Args: {e.args}")
        _, _, line = sys.exc_info
        print(f"The error is in line: {line}")

    final_coord, dist = calc_distance(coord_0, my_int_coord)
    print(f"Distance between {coord_0} and {my_int_coord}: {dist:.2f}")

    # Case 3 - Invalid string
    my_str_coord_2 = "abc,def,ghi"
    my_int_list_2 = my_str_coord_2.split(",")
    try:
        print(f'\nParsing invalid coordinates: "{my_str_coord_2}"')
        my_int_coord_2 = coord_cast(my_int_list_2)
        print(f"Parsed position: {my_int_coord}")
    except ValueError as e:
        print("❌ Upss... something went wrong while parsing coordinates 🤷")
        print(f"Error details - Type: {e.__class__.__name__}, Args: {e.args}")

    # Case 4 - Reading from command line i.e "(25,12,3)"
    # argv_len = ft_argv_len(sys.argv)
    # if argv_len == 1:
    #     pass
    # elif argv_len == 2:
    #     my_coord_list = [n for n in sys.argv[1].strip("()").split(",")]
    #     print(my_coord_list)
    # try:
    #     print("\nParsing from Command Line Argument")
    #     my_int_coord_2 = coord_cast(my_coord_list)
    #     print(f"Position created: {my_int_coord_2}")
    # except ValueError as e:
    #     print("❌ Upss... something went wrong while parsing coordinates 🤷")
    #     print(f"Error details - Type: {e.__class__.__name__},Args: {e.args}")
    #
    # final_coord, dist = calc_distance(coord_0, my_int_coord_2)
    # print(f"Distance between {coord_0} and {my_int_coord_2}: {dist:.2f}")

    print("\nUnpacking demonstration:")
    print(f"Player at x={final_coord[0]}, y={final_coord[1]}, "
          f"z={final_coord[2]}")
    print(f"Coordinates: x={final_coord[0]}, y={final_coord[1]}, "
          f"z={final_coord[2]}")

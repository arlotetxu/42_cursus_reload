#!/usr/bin/env python3


def garden_operations(error_type: int):
	if error_type == 1:
		int("abc")
	elif error_type == 2:
		1 / 0
	elif error_type == 3:
		with open("missing.txt", "r") as fd:
			pass
	elif error_type == 4:
		my_dict = {"0": 0}
		my_dict["_plant"]



def test_error_types():
	try:
		print("Testing ValueError...")
		garden_operations(1)
	except ValueError:
		print("Caught ValueError: invalid literal for int()\n")

	try:
		print("Testing ZeroDivisionError...")
		garden_operations(2)
	except ZeroDivisionError:
		print("Caught ZeroDivisionError: division by zero\n")

	try:
		print("Testing FileNotFoundError...")
		garden_operations(3)
	except FileNotFoundError:
		print("Caught FileNotFoundError: No such file 'missing.txt'\n")

	try:
		print("Testing KeyError...")
		garden_operations(4)
	except KeyError:
		print("Caught KeyError: 'missing\\_plant'\n")


	print("All error types tested successfully!")


if __name__ == "__main__":
	test_error_types()
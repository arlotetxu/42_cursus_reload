#!/usr/bin/env python3

import sys

num_args: int = len(sys.argv)
print("=== Command Quest ===")
if num_args == 1:
    print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    print(f"Total arguments: {num_args}")
elif num_args > 1:
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {num_args - 1}")
    i = 1
    while i < num_args:
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1
    print(f"Total arguments: {num_args}")

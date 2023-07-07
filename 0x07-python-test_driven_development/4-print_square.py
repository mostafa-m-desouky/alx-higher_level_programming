#!/usr/python3
"""This module contains a function that prints a square with the character #."""
import doctest


def print_square(size):
    """Function that prints a square with the character #.

    Args:
        size (int): Size of the square.

    Returns:
        None.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >=0")
    for row in range(size):
        print("#" * size)
if __name__ == "__main__":
    doctest.testfile("tests/4-print_square.txt")

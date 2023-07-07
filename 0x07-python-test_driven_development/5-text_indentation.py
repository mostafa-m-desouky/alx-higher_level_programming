#!/usr/bin/python3
"""This module contains a function that prints a text with 2 new lines after
each of these characters: ., ? and :."""
import doctest


def text_indentation(text):
    """Function that prints a text with 2 new lines after each of these
    characters: ., ? and :.

    Args:
        text (str): Text to be printed.

    Returns:
        None.

    Raises:
        TypeError: If text is not a string.

    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print(text[i])
            print()
        else:
            print(text[i], end="")
if __name__ == "__main__":
    doctest.testfile("tests/5-text_indentation.txt")

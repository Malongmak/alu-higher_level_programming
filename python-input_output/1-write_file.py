#!/usr/bin/python3
"""Are you documented ?"""


def write_file(filename="", text=""):
    """I document you"""
    with open(filename, 'w+') as f:
        return f.write(text)

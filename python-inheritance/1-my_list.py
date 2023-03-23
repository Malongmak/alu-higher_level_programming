#!/usr/bin/python3

"""A class that inherits."""


class MyList(list):
    """Contains list."""

    def print_sorted(self):
        """Prints sorted list."""

        sorted_list = sorted(self)
        print(sorted_list)

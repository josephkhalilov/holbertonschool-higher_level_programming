#!/usr/bin/python3
"""MyList class that inherits from list"""


class MyList(list):
    """Custom list class that can print a sorted version of itself"""

    def print_sorted(self):
        """Prints the list (ascending sorted) without modifying the original"""
        print(sorted(self))

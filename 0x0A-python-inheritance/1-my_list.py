#!/usr/bin/python3
"""defin class"""


class MyList(list):
    """MyList
    Args:
        list: list
    """
    def print_sorted(self):
        """Print"""
        list_ = self[:]
        list_.sort()
        print(list_)

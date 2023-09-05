#!/usr/bin/python3
"""defines module"""


class LockedClass:
    """LockedClass
    Attributes:
        first_name (str): first name of something.
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """instances"""

        self.first_name = "first_name"

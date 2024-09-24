#!/usr/bin/python3
"""
This module provides a VerboseList class that logs
operations when items are added, removed, or popped.
"""


class VerboseList(list):
    """
    class VerboseList inherited from list class
    """
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")

#!/bin/python3
"""
Extra. Implementing a Context Manager as a Class

A common use case of context managers is locking and unlocking resources and closing opened files.
Examples:
    - Containers
    - Database connections
    - Files
    - ...

Note: This module has been created for learning purposes.
More information in: https://book.pythontips.com/en/latest/context_managers.html
"""


class InnerObject:
    def __init__(self, size, weight):
        self.size = size
        self.weight = weight

    def print_info(self):
        print(f"The object has a size of {self.size} and a weight of {self.weight}")


class Context(object):
    def __init__(self, size, weight):
        self.obj = InnerObject(size, weight)

    def __enter__(self):
        return self.obj

    def __exit__(self, type, value, traceback):
        del self.obj


if __name__ == '__main__':
    with Context(50, 75) as created_object:
        created_object.print_info()

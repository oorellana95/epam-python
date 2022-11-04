#!/bin/python3
"""
2. Implement a Python decorator that ensures that all the arguments of the decorated function are of a certain type.
For example:

@ensure_argument_type(str)
def my_awesome_function(first_name, second_name):
    print('Hello {} {}'.format(first_name, second_name))

@ensure_argument_type(str)
my_awesome_function('Mike', 'Wazowski')  # Will allow the function to execute

@ensure_argument_type(str)
my_awesome_function('Mike', math.PI)  # Will raise an exception
"""


def ensure_argument_type(accepted_type):
    def decorator(function):
        def wrapper(*args):
            for arg in args:
                if isinstance(arg, accepted_type) is False:
                    raise TypeError(f"Arguments do not match the type {accepted_type}")
            function(*args)
        return wrapper
    return decorator


@ensure_argument_type(str)
def my_awesome_function(first_name, second_name):
    print('Hello {} {}'.format(first_name, second_name))


if __name__ == '__main__':
    my_awesome_function('Mike', 5)

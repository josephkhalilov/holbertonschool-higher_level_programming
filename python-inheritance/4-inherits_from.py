#!/usr/bin/python3
"""Return Tf a class that inherited from a_class."""


def inherits_from(obj, a_class):
    """Return Tf a class that inherited from a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class

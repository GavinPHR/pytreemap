#!/usr/bin/env python
"""TreeMap inner class.
"""
from pytreemap.abstract.map import Map
import pytreemap as tm

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'
__version__ = '0.4'
__status__ = 'Alpha'


class Entry(Map.Entry):
    """Node in the tree."""

    def __init__(self, key, value, parent):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.color = tm.TreeMap.BLACK

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value

    def set_value(self, value):
        """Replace the current value with the given value."""
        old_value = self.value
        self.value = value
        return old_value

    def equals(self, o):
        if not isinstance(o, Map.Entry):
            return False
        return (tm.TreeMap.val_equals(self.key, o.get_key()) and
                tm.TreeMap.val_equals(self.value, o.get_value()))

    __eq__ = equals

    def hash_code(self):
        key_hash = 0 if self.key is None else hash(self.key)
        value_hash = 0 if self.value is None else hash(self.value)
        return key_hash ^ value_hash

    __hash__ = hash_code

    def to_string(self):
        return str(self.key) + "=" + str(self.value)

    __repr__ = __str__ = to_string

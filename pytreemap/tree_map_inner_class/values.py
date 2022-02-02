#!/usr/bin/env python
"""TreeMap inner class.
"""
from pytreemap.abstract.abstract_collection import AbstractCollection

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'
__version__ = '0.4'
__status__ = 'Alpha'


class Values(AbstractCollection):
    """Value view class"""

    def __init__(self, tree_map):
        self.tm = tree_map

    def iterator(self):
        return self.tm.ValueIterator(self.tm.get_first_entry(), self.tm)

    __iter__ = iterator

    def size(self):
        return self.tm.size()

    __len__ = size

    def contains(self, o):
        return self.tm.contains_value(o)

    __contains__ = contains

    def remove(self, o):
        e = self.tm.get_first_entry()
        while e is not None:
            if self.tm.val_equals(e.get_value(), o):
                self.tm.delete_entry(e)
                return True
            self.tm.successor(e)
        return False

    def clear(self):
        self.tm.clear()

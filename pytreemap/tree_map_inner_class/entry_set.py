#!/usr/bin/env python
"""TreeMap inner class.
"""
from pytreemap.abstract.abstract_set import AbstractSet
from pytreemap.abstract.map import Map

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'
__version__ = '0.4'
__status__ = 'Alpha'


class EntrySet(AbstractSet):
    """Items view class"""

    def __init__(self, tree_map):
        self.tm = tree_map

    def iterator(self):
        return self.tm.EntryIterator(self.tm.get_first_entry(), self.tm)

    __iter__ = iterator

    def contains(self, o):
        if not isinstance(o, Map.Entry):
            return False
        entry = o
        value = entry.get_value()
        p = self.tm.get_entry(entry.get_key())
        return (p is not None and
                self.tm.val_equals(p.get_value(), value))

    __contains__ = contains

    def remove(self, o):
        if not isinstance(o, Map.Entry):
            return False
        entry = o
        value = entry.get_value()
        p = self.tm.get_entry(entry.get_key())
        if (p is not None and
                self.tm.val_equals(p.get_value(), value)):
            self.tm.delete_entry(p)
            return True
        return False

    def size(self):
        return self.tm.size()

    __len__ = size

    def clear(self):
        return self.tm.clear()

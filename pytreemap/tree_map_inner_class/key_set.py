#!/usr/bin/env python
"""TreeMap inner class.
"""
from pytreemap.abstract.abstract_set import AbstractSet
from pytreemap.abstract.navigable_set import NavigableSet

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'
__version__ = '0.4'
__status__ = 'Alpha'


class KeySet(NavigableSet, AbstractSet):
    """Keys view class"""

    def __init__(self, tree_map):
        self.m = tree_map

    def iterator(self):
        return self.m.key_iterator()

    __iter__ = iterator

    def descending_iterator(self):
        return self.m.descending_key_iterator()

    __reversed__ = descending_iterator

    def size(self): return self.m.size()
    __len__ = size
    def is_empty(self): return self.m.is_empty()
    def contains(self, o): return self.m.contains_key(o)
    __contains__ = contains
    def clear(self): self.m.clear()
    def lower(self, e): return self.m.lower_key(e)
    def floor(self, e): return self.m.floor_key(e)
    def ceiling(self, e): return self.m.ceiling_key(e)
    def higher(self, e): return self.m.higher_key(e)
    def first(self): return self.m.first_key()
    def last(self): return self.m.last_key()
    def comparator(self): return self.m.comparator()

    def poll_first(self):
        e = self.m.poll_first_entry()
        return None if e is None else e.get_key()

    def poll_last(self):
        e = self.m.poll_last_entry()
        return None if e is None else e.get_key()

    def remove(self, o):
        old_size = self.size()
        self.m.remove(o)
        return self.size() != old_size

    def sub_set(self, from_element, to_element,
                from_inclusive=True, to_inclusive=False):
        return KeySet(self.m.sub_map(from_element, to_element,
                                     from_inclusive, to_inclusive))

    def head_set(self, to_element, inclusive=False):
        return KeySet(self.m.head_map(to_element, inclusive))

    def tail_set(self, from_element, inclusive=True):
        return KeySet(self.m.tail_map(from_element, inclusive))

    def descending_set(self):
        return KeySet(self.m.descending_map())

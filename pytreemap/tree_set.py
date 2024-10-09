#!/usr/bin/env python
"""A Python implementation of the Java TreeSet.
"""
from pytreemap.tree_map import TreeMap
from .abstract.abstract_set import AbstractSet
from .abstract.navigable_set import NavigableSet

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'
__version__ = '0.4'
__status__ = 'Alpha'


class TreeSet(AbstractSet, NavigableSet):

    def __init__(self, comparator=None, m=None):
        """Pass comparator or m, not both.
        comparator is placed as the first arg to be
        consistent with TreeMap's constructor."""
        if m is not None:
            self.m = m
        else:
            self.m = TreeMap(comparator)
        self.PRESENT = object()

    def iterator(self):
        return self.m.navigable_key_set().iterator()

    __iter__ = iterator

    def descending_iterator(self):
        return self.m.descending_key_set().iterator()

    __reversed__ = descending_iterator

    def descending_set(self):
        return TreeSet(m=self.m.descending_map())

    def size(self):
        return self.m.size()

    __len__ = size

    def is_empty(self):
        return self.m.is_empty()

    def contains(self, o):
        return self.m.contains_key(o)

    __contains__ = contains

    def add(self, e):
        return self.m.put(e, self.PRESENT) is None

    def remove(self, o):
        return self.m.remove(o) is self.PRESENT

    def clear(self):
        self.m.clear()

    def sub_set(self, from_element, to_element,
                from_inclusive=True, to_inclusive=False):
        return TreeSet(m=self.m.sub_map(from_element, to_element,
                                      from_inclusive, to_inclusive))

    def head_set(self, to_element, inclusive=False):
        return TreeSet(m=self.m.head_map(to_element, inclusive))

    def tail_set(self, from_element, inclusive=True):
        return TreeSet(m=self.m.tail_map(from_element, inclusive))

    def comparator(self):
        return self.m.comparator()

    def first(self):
        return self.m.first_key()

    def last(self):
        return self.m.last_key()

    def lower(self, e):
        return self.m.lower_key(e)

    def floor(self, e):
        return self.m.floor_key(e)

    def ceiling(self, e):
        return self.m.ceiling_key(e)

    def higher(self, e):
        return self.m.higher_key(e)

    def poll_first(self):
        e = self.m.poll_first_entry()
        return None if e is None else e.get_key()

    def poll_last(self):
        e = self.m.poll_last_entry()
        return None if e is None else e.get_key()

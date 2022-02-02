#!/usr/bin/env python
"""TreeMap inner class.
"""
from .navigable_sub_map import NavigableSubMap
import pytreemap as ptm

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'
__version__ = '0.4'
__status__ = 'Alpha'


class DescendingSubMap(NavigableSubMap):

    def __init__(self, m,
                 from_start, lo, lo_inclusive,
                 to_end, hi, hi_inclusive):
        super().__init__(m,
                         from_start, lo, lo_inclusive,
                         to_end, hi, hi_inclusive)
        self.reverse_comparator = lambda a, b: self.m._comparator(b, a)

    def comparator(self):
        return self.reverse_comparator

    def sub_map(self, from_key, to_key,
                from_inclusive=True, to_inclusive=False):
        if not self.in_range(from_key, from_inclusive):
            raise KeyError('from_key out of range')
        if not self.in_range(to_key, to_inclusive):
            raise KeyError('to_key out of range')
        return DescendingSubMap(self.m,
                                False, to_key, to_inclusive,
                                False, from_key, from_inclusive)

    def head_map(self, to_key, inclusive=False):
        if not self.in_range(to_key, inclusive):
            raise KeyError('to_key out of range')
        return DescendingSubMap(self.m,
                                False, to_key, inclusive,
                                self.to_end, self.hi, self.hi_inclusive)

    def tail_map(self, from_key, inclusive=True):
        if not self.in_range(from_key, inclusive):
            raise KeyError('from_key out of range')
        return DescendingSubMap(self.m,
                                self.from_start, self.lo, self.lo_inclusive,
                                False, from_key, inclusive)

    def descending_map(self):
        if self.descending_map_view is None:
            self.descending_map_view = \
                ptm.AscendingSubMap(self.m,
                                    self.from_start, self.lo, self.lo_inclusive,
                                    self.to_end, self.hi, self.hi_inclusive)
        return self.descending_map_view

    def key_iterator(self):
        return super().DescendingSubMapKeyIterator(self.abs_highest(),
                                                   self.abs_low_fence(),
                                                   self)

    __iter__ = key_iterator

    def descending_key_iterator(self):
        return super().SubMapKeyIterator(self.abs_lowest(),
                                         self.abs_high_fence(),
                                         self)

    __reversed__ = descending_key_iterator

    class DescendingEntrySetView(NavigableSubMap.EntrySetView):

        def iterator(self):
            return NavigableSubMap. \
                DescendingSubMapEntryIterator(self.outer.abs_highest(),
                                              self.outer.abs_low_fence(),
                                              self.outer)

        __iter__ = iterator

    def entry_set(self):
        if self.entry_set_view is None:
            self.entry_set_view = self.DescendingEntrySetView(self)
        return self.entry_set_view

    def sub_lowest(self): return self.abs_highest()
    def sub_highest(self): return self.abs_lowest()
    def sub_ceiling(self, key): return self.abs_floor(key)
    def sub_higher(self, key): return self.abs_lower(key)
    def sub_floor(self, key): return self.abs_ceiling(key)
    def sub_lower(self, key): return self.abs_higher(key)

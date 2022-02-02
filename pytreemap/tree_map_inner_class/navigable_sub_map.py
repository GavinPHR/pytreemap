#!/usr/bin/env python
"""TreeMap inner class.
"""
from abc import abstractmethod
from collections.abc import Iterator
import pytreemap as ptm
from pytreemap.abstract.map import Map
from pytreemap.abstract.navigable_map import NavigableMap
from pytreemap.abstract.abstract_map import AbstractMap
from pytreemap.abstract.abstract_set import AbstractSet

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'
__version__ = '0.4'
__status__ = 'Alpha'


class NavigableSubMap(AbstractMap, NavigableMap):

    def __init__(self, m,
                 from_start, lo, lo_inclusive,
                 to_end, hi, hi_inclusive):
        if not from_start and not to_end:
            if m.compare(lo, hi) > 0:
                raise KeyError('from_key > to_key')
        else:
            if not from_start:
                m.compare(lo, lo)
            if not to_end:
                m.compare(hi, hi)
        self.m = m
        self.lo, self.hi = lo, hi
        self.from_start, self.to_end = from_start, to_end
        self.lo_inclusive, self.hi_inclusive = lo_inclusive, hi_inclusive
        self.descending_map_view = None
        self.entry_set_view = None
        self.navigable_key_set_view = None
        super().__init__()

    def too_low(self, key):
        if not self.from_start:
            c = self.m.compare(key, self.lo)
            if c < 0 or (c == 0 and not self.lo_inclusive):
                return True
        return False

    def too_high(self, key):
        if not self.to_end:
            c = self.m.compare(key, self.hi)
            if c > 0 or (c == 0 and not self.hi_inclusive):
                return True
        return False

    def in_range(self, key, inclusive=True):
        if not inclusive:
            return self.in_closed_range(key)
        return not self.too_low(key) and not self.too_high(key)

    def in_closed_range(self, key):
        return ((self.from_start or self.m.compare(key, self.lo) >= 0) and
                (self.to_end or self.m.compare(self.hi, key) >= 0))

    def abs_lowest(self):
        e = (self.m.get_first_entry() if self.from_start else
             (self.m.get_ceiling_entry(self.lo) if self.lo_inclusive else
              self.m.get_higher_entry(self.lo)))
        return None if e is None or self.too_high(e.key) else e

    def abs_highest(self):
        e = (self.m.get_last_entry() if self.to_end else
             (self.m.get_floor_entry(self.hi) if self.hi_inclusive else
              self.m.get_lower_entry(self.hi)))
        return None if e is None or self.too_low(e.key) else e

    def abs_ceiling(self, key):
        if self.too_low(key):
            return self.abs_lowest()
        e = self.m.get_ceiling_entry(key)
        return None if e is None or self.too_high(e.key) else e

    def abs_higher(self, key):
        if self.too_low(key):
            return self.abs_lowest()
        e = self.m.get_higher_entry(key)
        return None if e is None or self.too_high(e.key) else e

    def abs_floor(self, key):
        if self.too_high(key):
            return self.abs_highest()
        e = self.m.get_floor_entry(key)
        return None if e is None or self.too_low(e.key) else e

    def abs_lower(self, key):
        if self.too_high(key):
            return self.abs_highest()
        e = self.m.get_lower_entry(key)
        return None if e is None or self.too_low(e.key) else e

    def abs_high_fence(self):
        return (None if self.to_end else
                (self.m.get_higher_entry(self.hi) if self.hi_inclusive else
                 self.m.get_ceiling_entry(self.hi)))

    def abs_low_fence(self):
        return (None if self.from_start else
                (self.m.get_lower_entry(self.lo) if self.lo_inclusive else
                 self.m.get_floor_entry(self.lo)))

    @abstractmethod
    def sub_lowest(self):
        raise NotImplementedError

    @abstractmethod
    def sub_highest(self):
        raise NotImplementedError

    @abstractmethod
    def sub_ceiling(self, key):
        raise NotImplementedError

    @abstractmethod
    def sub_higher(self, key):
        raise NotImplementedError

    @abstractmethod
    def sub_floor(self, key):
        raise NotImplementedError

    @abstractmethod
    def sub_lower(self, key):
        raise NotImplementedError

    @abstractmethod
    def key_iterator(self):
        raise NotImplementedError

    __iter__ = key_iterator

    @abstractmethod
    def descending_key_iterator(self):
        raise NotImplementedError

    __reversed__ = descending_key_iterator

    def is_empty(self):
        return (self.m.is_empty()
                if self.from_start and self.to_end
                else self.entry_set().is_empty())

    def size(self):
        return (self.m.size()
                if self.from_start and self.to_end
                else self.entry_set().size())

    __len__ = size

    def contains_key(self, key):
        return self.in_range(key) and self.m.contains_key(key)

    __contains__ = contains_key

    def put(self, key, value):
        if not self.in_range(key):
            raise KeyError('key out of range')
        return self.m.put(key, value)

    __setitem__ = put

    def get(self, key):
        return None if not self.in_range(key) else self.m.get(key)

    def __getitem__(self, key):
        if not self.in_range(key):
            raise KeyError('key out of range')
        return self.m.__getitem__(key)

    def remove(self, key):
        return None if not self.in_range(key) else self.m.remove(key)

    def __delitem__(self, key):
        if not self.in_range(key):
            raise KeyError('key out of range')
        return self.m.__delitem__(key)

    def ceiling_entry(self, key):
        return ptm.TreeMap.export_entry(self.sub_ceiling(key))

    def ceiling_key(self, key):
        return ptm.TreeMap.key_or_none(self.sub_ceiling(key))

    def higher_entry(self, key):
        return ptm.TreeMap.export_entry(self.sub_higher(key))

    def higher_key(self, key):
        return ptm.TreeMap.key_or_none(self.sub_higher(key))

    def floor_entry(self, key):
        return ptm.TreeMap.export_entry(self.sub_floor(key))

    def floor_key(self, key):
        return ptm.TreeMap.key_or_none(self.sub_floor(key))

    def lower_entry(self, key):
        return ptm.TreeMap.export_entry(self.sub_lower(key))

    def lower_key(self, key):
        return ptm.TreeMap.key_or_none(self.sub_lower(key))

    def first_key(self):
        return ptm.TreeMap.key(self.sub_lowest())

    def last_key(self):
        return ptm.TreeMap.key(self.sub_highest())

    def first_entry(self):
        return ptm.TreeMap.export_entry(self.sub_lowest())

    def last_entry(self):
        return ptm.TreeMap.export_entry(self.sub_highest())

    def poll_first_entry(self):
        e = self.sub_lowest()
        result = ptm.TreeMap.export_entry(e)
        if e is not None:
            self.m.delete_entry(e)
        return result

    def poll_last_entry(self):
        e = self.sub_highest()
        result = ptm.TreeMap.export_entry(e)
        if e is not None:
            self.m.delete_entry(e)
        return result

    def navigable_key_set(self):
        nksv = self.navigable_key_set_view
        return nksv if nksv is not None else ptm.TreeMap.KeySet(self)

    def key_set(self):
        return self.navigable_key_set()

    def descending_key_set(self):
        return self.descending_map().navigable_key_set()

    class EntrySetView(AbstractSet):

        def __init__(self, outer):
            self.outer = outer
            self._size = -1
            self.size_mod_count = 0

        def size(self):
            if self.outer.from_start and self.outer.to_end:
                return self.outer.m.size()
            if (self._size == -1 or
                    self.size_mod_count != self.outer.m._mod_count):
                self.size_mod_count = self.outer.m._mod_count
                self._size = 0
                i = iter(self)
                for _ in i:
                    self._size += 1
            return self._size

        __len__ = size

        def is_empty(self):
            n = self.outer.abs_lowest()
            return n is None or self.outer.too_high(n.key)

        def contains(self, o):
            if not isinstance(o, Map.Entry):
                return False
            entry = o
            key = entry.get_key()
            if not self.outer.in_range(key):
                return False
            node = self.outer.m.get_entry(key)
            return (node is not None and
                    ptm.TreeMap.val_equals(node.get_value(), entry.get_value()))

        __contains__ = contains

        def remove(self, o):
            if not isinstance(o, Map.Entry):
                return False
            entry = o
            key = entry.get_key()
            if not self.outer.in_range(key):
                return False
            node = self.outer.m.get_entry(key)
            if (node is not None and
                    ptm.TreeMap.val_equals(node.get_value(),
                                           entry.get_value())):
                self.outer.m.delete_entry(node)
                return True
            return False

    class SubMapIterator(Iterator):

        def __init__(self, first, fence, outer):
            self.outer = outer
            self.expected_mod_count = outer.m._mod_count
            self.last_returned = None
            self.next_ = first
            self.fence_key = object() if fence is None else fence.key

        def has_next(self):
            return (self.next_ is not None and
                    self.next_.key is not self.fence_key)

        def next_entry(self):
            e = self.next_
            if e is None or e.key is self.fence_key:
                raise StopIteration
            if self.outer.m._mod_count != self.expected_mod_count:
                raise RuntimeError
            self.next_ = ptm.TreeMap.successor(e)
            self.last_returned = e
            return e

        def prev_entry(self):
            e = self.next_
            if e is None or e.key is self.fence_key:
                raise StopIteration
            if self.outer.m._mod_count != self.expected_mod_count:
                raise RuntimeError
            self.next_ = ptm.TreeMap.predecessor(e)
            self.last_returned = e
            return e

        def remove_ascending(self):
            if self.last_returned is None:
                raise RuntimeError
            if self.outer.m._mod_count != self.expected_mod_count:
                raise RuntimeError
            if (self.last_returned.left is not None and
                    self.last_returned.right is not None):
                self.next_ = self.last_returned
            self.outer.m.delete_entry(self.last_returned)
            self.last_returned = None
            self.expected_mod_count = self.outer.m._mod_count

        def remove_descending(self):
            if self.last_returned is None:
                raise RuntimeError
            if self.outer.m._mod_count != self.expected_mod_count:
                raise RuntimeError
            self.outer.m.delete_entry(self.last_returned)
            self.last_returned = None
            self.expected_mod_count = self.outer.m._mod_count

    class SubMapEntryIterator(SubMapIterator):

        def __init__(self, first, fence, outer):
            super().__init__(first, fence, outer)

        def next(self):
            return self.next_entry()

        __next__ = next

        def remove(self):
            self.remove_ascending()

    class SubMapKeyIterator(SubMapIterator):

        def __init__(self, first, fence, outer):
            super().__init__(first, fence, outer)

        def next(self):
            return self.next_entry().key

        __next__ = next

        def remove(self):
            self.remove_ascending()

    class DescendingSubMapEntryIterator(SubMapIterator):

        def __init__(self, last, fence, outer):
            super().__init__(last, fence, outer)

        def next(self):
            return self.prev_entry()

        __next__ = next

        def remove(self):
            self.remove_descending()

    class DescendingSubMapKeyIterator(SubMapIterator):

        def __init__(self, last, fence, outer):
            super().__init__(last, fence, outer)

        def next(self):
            return self.prev_entry().key

        __next__ = next

        def remove(self):
            self.remove_descending()

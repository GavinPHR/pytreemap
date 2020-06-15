#!/usr/bin/env python
"""TreeMap inner class.
"""
from pytreemap.exception import ConcurrentModificationError, IllegalStateError

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'
__version__ = '0.1'
__status__ = 'Alpha'


class PrivateEntryIterator:

    def __init__(self, first, tree_map):
        self.tm = tree_map
        self.expected_mod_count = tree_map.mod_count
        self.last_returned = None
        self.next = first

    def __iter__(self):
        return self

    def has_next(self):
        return self.next is not None

    def next_entry(self):
        e = self.next
        if e is None:
            raise StopIteration
        if self.tm.mod_count != self.expected_mod_count:
            raise ConcurrentModificationError
        self.next = self.tm.successor(e)
        self.last_returned = e
        return e

    def prev_entry(self):
        e = self.next
        if e is None:
            raise StopIteration
        if self.tm.mod_count != self.expected_mod_count:
            raise ConcurrentModificationError
        self.next = self.tm.predecessor(e)
        self.last_returned = e
        return e

    def remove(self):
        if self.last_returned is None:
            raise IllegalStateError
        if self.tm.mod_count != self.expected_mod_count:
            raise ConcurrentModificationError
        if (self.last_returned.left is not None and
                self.last_returned.right is not None):
            # Because the content of the last_returned node
            # is replaced by the next node's content.
            self.next = self.last_returned
        self.tm.delete_entry(self.last_returned)
        self.expected_mod_count = self.tm.mod_count
        self.last_returned = None

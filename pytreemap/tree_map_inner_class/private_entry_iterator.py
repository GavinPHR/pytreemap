#!/usr/bin/env python
"""TreeMap inner class.
"""

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'
__version__ = '0.4'
__status__ = 'Alpha'


class PrivateEntryIterator:

    def __init__(self, first, tree_map):
        self.tm = tree_map
        self.expected_mod_count = tree_map._mod_count
        self.last_returned = None
        self.next_ = first

    def __iter__(self):
        return self

    def has_next(self):
        return self.next_ is not None

    def next_entry(self):
        e = self.next_
        if e is None:
            raise StopIteration
        if self.tm._mod_count != self.expected_mod_count:
            raise RuntimeError
        self.next_ = self.tm.successor(e)
        self.last_returned = e
        return e

    def prev_entry(self):
        e = self.next_
        if e is None:
            raise StopIteration
        if self.tm._mod_count != self.expected_mod_count:
            raise RuntimeError
        self.next_ = self.tm.predecessor(e)
        self.last_returned = e
        return e

    def remove(self):
        if self.last_returned is None:
            raise RuntimeError
        if self.tm._mod_count != self.expected_mod_count:
            raise RuntimeError
        if (self.last_returned.left is not None and
                self.last_returned.right is not None):
            # Because the content of the last_returned node
            # is replaced by the next node's content.
            self.next_ = self.last_returned
        self.tm.delete_entry(self.last_returned)
        self.expected_mod_count = self.tm._mod_count
        self.last_returned = None

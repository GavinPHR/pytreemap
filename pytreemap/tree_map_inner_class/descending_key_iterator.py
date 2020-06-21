#!/usr/bin/env python
"""TreeMap inner class.
"""
from .private_entry_iterator import PrivateEntryIterator

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'
__version__ = '0.4'
__status__ = 'Alpha'


class DescendingKeyIterator(PrivateEntryIterator):

    def __init__(self, first, tree_map):
        super().__init__(first, tree_map)

    def next(self):
        return self.prev_entry().key

    __next__ = next

    def remove(self):
        if self.last_returned is None:
            raise RuntimeError
        if self.tm._mod_count != self.expected_mod_count:
            raise RuntimeError
        self.tm.delete_entry(self.last_returned)
        self.last_returned = None
        self.expected_mod_count = self.tm._mod_count

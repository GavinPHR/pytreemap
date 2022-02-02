#!/usr/bin/env python
"""TreeMap inner class.
"""
from .private_entry_iterator import PrivateEntryIterator

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'
__version__ = '0.4'
__status__ = 'Alpha'


class ValueIterator(PrivateEntryIterator):

    def __init__(self, first, tree_map):
        super().__init__(first, tree_map)

    def next(self):
        return self.next_entry().value

    __next__ = next

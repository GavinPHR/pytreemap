#!/usr/bin/env python
from pytreemap import TreeMap

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'

class Comparable(object):
    def __lt__(self, other):
        return hash(self) < hash(other)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return super().__hash__()

TEST_SIZE = 100
entry_data = [[Comparable() for _ in range(TEST_SIZE)],
              [object() for _ in range(TEST_SIZE)]]
map = TreeMap()

def test():
    for i in range(TEST_SIZE):
        map.put(entry_data[0][i], entry_data[1][i])
    for e in map.entry_set():
        key = e.get_key()
        value = e.get_value()
        expected_entry_hash_code = hash(key) ^ hash(value)
        assert hash(e) == expected_entry_hash_code



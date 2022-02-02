#!/usr/bin/env python
import pytest
from pytreemap import TreeMap

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'


TEST_SIZE = 5000
KEYS = [each for each in range(TEST_SIZE)]
VALUES = [each+TEST_SIZE for each in range(TEST_SIZE)]


def test_map():
    map = TreeMap()
    for each in range(TEST_SIZE):
        map.put(KEYS[each], VALUES[each])
    keys = map.key_set().to_list()
    keys.sort()
    for each in range(TEST_SIZE):
        assert keys[each] == KEYS[each]
    values = map.values().to_list()
    values.sort()
    for each in range(TEST_SIZE):
        assert values[each] == VALUES[each]
    entries = map.entry_set().to_list()
    entries.sort(key=lambda e: e.get_key())
    for each in range(TEST_SIZE):
        assert (entries[each].get_key() == KEYS[each] and
                entries[each].get_value() == VALUES[each])

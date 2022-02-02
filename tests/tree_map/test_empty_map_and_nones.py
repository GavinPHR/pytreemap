#!/usr/bin/env python
import pytest
from pytreemap import TreeMap

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'


def test():
    comparable = TreeMap()
    with pytest.raises(TypeError):
        comparable.put(None, 'anything')
    comparable.put('test', 'anything')
    with pytest.raises(TypeError):
        comparable.put(None, 'anything')

    def case_insensitive_order(a, b):
        x, y = a.lower(), b.lower()
        if x < y:
            return -1
        elif x > y:
            return 1
        else:
            return 0

    comparator = TreeMap(case_insensitive_order)
    with pytest.raises(Exception):
        comparator.put(None, 'anything')
    comparator.put('test', 'anything')
    with pytest.raises(Exception):
        comparator.put(None, 'anything')
    comparator.clear()
    with pytest.raises(Exception):
        comparator.put(object(), 'anything')

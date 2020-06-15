#!/usr/bin/env python
import pytest
from pytreemap import TreeMap

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'


def test():
    def case_insensitive_order(a, b):
        x, y = a.lower(), b.lower()
        if x < y:
            return -1
        elif x > y:
            return 1
        else:
            return 0
    # TypeError is raised when objects cannot be compared naturally
    with pytest.raises(TypeError):
        m = TreeMap()
        m.head_map(object())
    with pytest.raises(TypeError):
        m = TreeMap()
        m.tail_map(object())
    # AttributeError is raised because non-string has no lower() method
    with pytest.raises(AttributeError):
        m = TreeMap(case_insensitive_order)
        m.head_map(0)
    with pytest.raises(AttributeError):
        m = TreeMap(case_insensitive_order)
        m.tail_map(0)
    with pytest.raises(TypeError):
        m = TreeMap()
        m.head_map(None)
    with pytest.raises(TypeError):
        m = TreeMap()
        m.tail_map(None)
    with pytest.raises(AttributeError):
        m = TreeMap(case_insensitive_order)
        m.head_map(None)
    with pytest.raises(AttributeError):
        m = TreeMap(case_insensitive_order)
        m.tail_map(None)
    m = TreeMap()
    m.head_map(0)
    m.tail_map(0)
    m = TreeMap(case_insensitive_order)
    m.head_map('peng')
    m.tail_map('peng')

#!/usr/bin/env python
from pytreemap import TreeMap

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'


def test():
    map = TreeMap()
    assert not map.contains_value('haoranpeng')
    assert not map.contains_value(None)

    map.put('a', None)
    map.put('b', 'haoranpeng')

    assert map.contains_value('haoranpeng')
    assert map.contains_value(None)

#!/usr/bin/env python
import pytest
from pytreemap import TreeMap

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'

m = TreeMap()
for i in range(18):
    m.put(i, i)

@pytest.mark.parametrize('c',
                         [m.values(), m.key_set(), m.entry_set()])
def test(c):
    it = iter(c)
    with pytest.raises(StopIteration):
        while True:
            next(it)

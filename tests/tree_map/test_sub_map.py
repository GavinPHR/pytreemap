#!/usr/bin/env python
import pytest
from pytreemap import TreeMap

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'


def test():
    m = TreeMap()
    m.put(1, 1)
    m.put(2, 2)
    m.put(3, 3)
    m2 = m.sub_map(2, 2)
    with pytest.raises(KeyError):
        m2.first_key()
    with pytest.raises(KeyError):
        m2.last_key()
    m3 = m.sub_map(2, 3)
    assert m3.first_key() == 2
    assert m3.last_key() == 2

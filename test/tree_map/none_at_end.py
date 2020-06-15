#!/usr/bin/env python
from pytreemap import TreeMap

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'


def none_at_end(x, y):
    if x is None and y is None:
        return 0
    if x is None and y is not None:
        return 1
    if x is not None and y is None:
        return -1
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0


def test():
    m1 = TreeMap(none_at_end)
    assert m1.put('a', 'a') is None
    assert m1.put('b', 'b') is None
    assert m1.put('c', 'c') is None
    assert m1.put(None, 'd') is None

    m2 = TreeMap(none_at_end)
    m2.put_all(m1)

    assert m1.last_key() is None
    assert m1.get(m1.last_key()) == 'd'
    assert m1.remove(m1.last_key()) == 'd'
    assert m1.last_key() == 'c'

    assert m2.entry_set().to_string() == '[a=a, b=b, c=c, None=d]'

    m3 = m2.tail_map('b')

    assert m3.last_key() is None
    assert m3.get(m3.last_key()) == 'd'
    assert m3.remove(m3.last_key()) == 'd'
    assert m3.last_key() == 'c'

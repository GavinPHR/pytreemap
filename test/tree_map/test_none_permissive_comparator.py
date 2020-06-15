#!/usr/bin/env python
from pytreemap import TreeMap

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'


def none_low(x, y):
    if x is y:
        return 0
    elif x is None:
        return -1
    elif y is None:
        return 1
    else:
        if x < y:
            return -1
        elif x > y:
            return 1
        else:
            return 0


def none_high(x, y):
    if x is y:
        return 0
    elif x is None:
        return 1
    elif y is None:
        return -1
    else:
        if x < y:
            return -1
        elif x > y:
            return 1
        else:
            return 0


def test():
    m = TreeMap(none_low)

    m.put('a', 'A')
    m.put('b', 'B')
    m.put('c', 'C')

    assert m.to_string() == '{a=A, b=B, c=C}'
    assert m.head_map('b').to_string() == '{a=A}'
    assert m.tail_map('b').to_string() == '{b=B, c=C}'
    assert m.head_map(None).to_string() == '{}'
    assert m.tail_map(None).to_string() == '{a=A, b=B, c=C}'

    m = TreeMap(none_high)

    m.put('a', 'A')
    m.put('b', 'B')
    m.put('c', 'C')

    assert m.to_string() == '{a=A, b=B, c=C}'
    assert m.head_map('b').to_string() == '{a=A}'
    assert m.tail_map('b').to_string() == '{b=B, c=C}'
    assert m.head_map(None).to_string() == '{a=A, b=B, c=C}'
    assert m.tail_map(None).to_string() == '{}'

    m.put(None, 'NONE')

    assert m.to_string() == '{a=A, b=B, c=C, None=NONE}'
    assert m.head_map('b').to_string() == '{a=A}'
    assert m.tail_map('b').to_string() == '{b=B, c=C, None=NONE}'
    assert m.head_map(None).to_string() == '{a=A, b=B, c=C}'
    assert m.tail_map(None).to_string() == '{None=NONE}'

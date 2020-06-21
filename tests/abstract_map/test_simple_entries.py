#!/usr/bin/env python
import pytest
from pytreemap.abstract.abstract_map import AbstractMap

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'


k = 'foo'
v = 1
v2 = 2


@pytest.mark.parametrize('e',
                         [AbstractMap.SimpleEntry(k, v),
                          AbstractMap.SimpleImmutableEntry(k, v)])
def test_entry(e):
    assert e.get_key() == k
    assert e.get_value() == v
    assert e == AbstractMap.SimpleEntry(k, v)
    assert e != AbstractMap.SimpleEntry(k, v2)
    assert e is not None
    assert e == AbstractMap.SimpleImmutableEntry(k, v)
    assert e.to_string() == str(k)+'='+str(v)
    if isinstance(e, AbstractMap.SimpleEntry):
        assert e.set_value(v2) == v
        assert e.get_value() == v2
        assert e.set_value(None) == v2
        assert e.get_value() is None
    else:
        with pytest.raises(NotImplementedError):
            e.set_value(v2)


@pytest.mark.parametrize('e',
                         [AbstractMap.SimpleEntry(None, None),
                          AbstractMap.SimpleImmutableEntry(None, None)])
def test_none_entry(e):
    assert e.get_key() is None
    assert e.get_value() is None
    assert e == AbstractMap.SimpleEntry(None, None)
    assert e == AbstractMap.SimpleImmutableEntry(None, None)
    assert e.to_string() == 'None=None'
    if isinstance(e, AbstractMap.SimpleEntry):
        assert e.set_value(v) is None
        assert e.get_value() == v
    else:
        with pytest.raises(NotImplementedError):
            e.set_value(None)

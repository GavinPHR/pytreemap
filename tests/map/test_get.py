#!/usr/bin/env python
import pytest
from pytreemap import TreeMap

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'


def put(m, key, value, old_value):
    if old_value is not None:
        assert m.contains_value(old_value)
        assert m.values().contains(old_value)
    assert m.put(key, value) == old_value
    assert m.get(key) == value
    assert m.contains_key(key)
    assert m.key_set().contains(key)
    assert m.contains_value(value)
    assert m.values().contains(value)
    assert not m.is_empty()


def test_get():
    m = TreeMap()
    # permitsNullKeys=False, permitsNullValues=True, usesIdentity=False
    put(m, 'A', True, None)
    put(m, 'A', False, True)
    put(m, 'B', True, None)
    put(m, 'A', False, False)

    try:
        m.get(None)
        pytest.fail('did not reject None key')
    except TypeError:
        pass
    except Exception as e:
        print('unexpected exception')
        raise e

    try:
        m.put(None, True)
        pytest.fail('did not reject None key')
    except TypeError:
        pass
    except Exception as e:
        print('unexpected exception')
        raise e

    try:
        put(m, 'C', None, None)
        put(m, 'C', True, None)
        put(m, 'C', None, True)
    except Exception as e:
        print('unexpected exception')
        raise e

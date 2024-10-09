#!/usr/bin/env python
import pytest
from pytreemap import TreeSet

__author__ = 'Sascha Holzhauer'
__email__ = 'Sascha.Holzhauer@uni-kassel.de'
__license__ = 'GPL-2.0'

def test():
        
    m = TreeSet()
    m.add(1)
    m.add(2)
    m.add(3)
    m.add(4)
    
    m2 = m.tail_set(4, inclusive=False)
    with pytest.raises(KeyError):
        m2.first()
    with pytest.raises(KeyError):
        m2.last()
        
    m3 = m.tail_set(3, inclusive=False)
    assert m3.first() == 4
    assert m3.last() == 4

    m4 = m.tail_set(3, inclusive=True)
    assert m4.first() == 3
    assert m4.last() == 4

    m5 = m.tail_set(2, inclusive=False)
    assert m5.first() == 3
    assert m5.last() == 4

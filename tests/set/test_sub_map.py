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
    
    m2 = m.sub_set(2, 2, from_inclusive=True, to_inclusive=False)
    with pytest.raises(KeyError):
        m2.first()
    with pytest.raises(KeyError):
        m2.last()
        
    m3 = m.sub_set(2, 3, from_inclusive=True, to_inclusive=False)
    assert m3.first() == 2
    assert m3.last() == 2

    m4 = m.sub_set(2, 3, from_inclusive=True, to_inclusive=True)
    assert m4.first() == 2
    assert m4.last() == 3

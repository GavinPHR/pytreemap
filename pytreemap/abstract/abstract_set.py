#!/usr/bin/env python
"""A Python implementation of the Java AbstractSet interface.
"""
from .abstract_collection import AbstractCollection
from .set import Set

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'
__version__ = '0.4'
__status__ = 'Alpha'


class AbstractSet(AbstractCollection, Set):

    def equals(self, o):
        if o is self:
            return True
        if not isinstance(o, Set):
            return False
        c = o
        if c.size() != self.size():
            return False
        try:
            return self.contains_all(c)
        except TypeError:
            return False

    __eq__ = equals

    def hash_code(self):
        h = 0
        i = iter(self)
        for obj in i:
            if obj is not None:
                h += hash(obj)
        return h

    __hash__ = hash_code

    def remove_all(self, c):
        modified = False
        if self.size() > c.size():
            for e in c:
                modified = modified or self.remove(e)
        else:
            i = iter(self)
            for e in i:
                if c.contains(e):
                    i.remove()
                    modified = True
        return modified

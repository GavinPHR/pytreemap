#!/usr/bin/env python
"""A Python implementation of the Java AbstractCollection interface.
"""
from abc import abstractmethod
from .collection import Collection

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'
__version__ = '0.4'
__status__ = 'Alpha'


class AbstractCollection(Collection):

    @abstractmethod
    def iterator(self):
        raise NotImplementedError

    __iter__ = iterator

    @abstractmethod
    def size(self):
        raise NotImplementedError

    __len__ = size

    def is_empty(self):
        return self.size() == 0

    def contains(self, o):
        it = iter(self)
        if o is None:
            for e in it:
                if e is None:
                    return True
        else:
            for e in it:
                if o == e:
                    return True
        return False

    __contains__ = contains

    def to_list(self):
        return [e for e in iter(self)]

    def add(self, e):
        raise NotImplementedError

    def remove(self, o):
        it = iter(self)
        if o is None:
            for e in it:
                if e is None:
                    it.remove()
                    return True
        else:
            for e in it:
                if o == e:
                    it.remove()
                    return True
        return False

    def contains_all(self, c):
        for e in c:
            if not self.contains(e):
                return False
        return True

    def add_all(self, c):
        modified = False
        for e in c:
            if self.add(e):
                modified = True
        return modified

    def remove_all(self, c):
        modified = False
        it = iter(self)
        for e in it:
            if c.contains(e):
                it.remove()
                modified = True
        return modified

    def retain_all(self, c):
        modified = False
        it = iter(self)
        for e in it:
            if not c.contains(e):
                it.remove()
                modified = True
        return modified

    def clear(self):
        it = iter(self)
        for _ in it:
            it.remove()

    def to_string(self):
        s = ['[']
        for e in self:
            s.append('(this Collection)' if e is self else str(e))
            s.append(', ')
        if s[-1] == '[':
            s.append(']')
        else:
            s[-1] = ']'
        return "".join(s)

    __repr__ = __str__ = to_string

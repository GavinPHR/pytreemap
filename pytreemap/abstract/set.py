#!/usr/bin/env python
"""A Python implementation of the Java Set interface.
"""
from abc import abstractmethod
from .collection import Collection

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'
__version__ = '0.4'
__status__ = 'Alpha'


class Set(Collection):

    @abstractmethod
    def size(self):
        raise NotImplementedError

    __len__ = size

    @abstractmethod
    def is_empty(self):
        raise NotImplementedError

    @abstractmethod
    def contains(self, o):
        raise NotImplementedError

    __contains__ = contains

    @abstractmethod
    def iterator(self):
        raise NotImplementedError

    __iter__ = iterator

    @abstractmethod
    def to_list(self):
        raise NotImplementedError

    @abstractmethod
    def add(self, e):
        raise NotImplementedError

    @abstractmethod
    def remove(self, o):
        raise NotImplementedError

    @abstractmethod
    def contains_all(self, c):
        raise NotImplementedError

    @abstractmethod
    def add_all(self, c):
        raise NotImplementedError

    @abstractmethod
    def remove_all(self, c):
        raise NotImplementedError

    @abstractmethod
    def clear(self):
        raise NotImplementedError

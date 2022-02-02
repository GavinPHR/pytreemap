#!/usr/bin/env python
"""A Python implementation of the Java SortedMap interface.
"""
from abc import abstractmethod
from .map import Map

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'
__version__ = '0.4'
__status__ = 'Alpha'


class SortedMap(Map):

    @abstractmethod
    def comparator(self):
        raise NotImplementedError

    @abstractmethod
    def sub_map(self, from_key, to_key):
        raise NotImplementedError

    @abstractmethod
    def head_map(self, to_key):
        raise NotImplementedError

    @abstractmethod
    def tail_map(self, from_key):
        raise NotImplementedError

    @abstractmethod
    def first_key(self):
        raise NotImplementedError

    @abstractmethod
    def last_key(self):
        raise NotImplementedError

    @abstractmethod
    def key_set(self):
        raise NotImplementedError

    @abstractmethod
    def values(self):
        raise NotImplementedError

    @abstractmethod
    def entry_set(self):
        raise NotImplementedError

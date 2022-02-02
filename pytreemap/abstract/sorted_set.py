#!/usr/bin/env python
"""A Python implementation of the Java SortedSet interface.
"""
from abc import abstractmethod
from .set import Set

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'
__version__ = '0.4'
__status__ = 'Alpha'


class SortedSet(Set):

    @abstractmethod
    def comparator(self):
        raise NotImplementedError

    @abstractmethod
    def sub_set(self, from_element, to_element):
        raise NotImplementedError

    @abstractmethod
    def head_set(self, to_element):
        raise NotImplementedError

    @abstractmethod
    def tail_set(self, from_element):
        raise NotImplementedError

    @abstractmethod
    def first(self):
        raise NotImplementedError

    @abstractmethod
    def last(self):
        raise NotImplementedError

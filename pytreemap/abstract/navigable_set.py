#!/usr/bin/env python
"""A Python implementation of the Java NavigableSet interface.
"""
from abc import abstractmethod
from .sorted_set import SortedSet

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'
__version__ = '0.4'
__status__ = 'Alpha'


class NavigableSet(SortedSet):

    @abstractmethod
    def lower(self, e):
        raise NotImplementedError

    @abstractmethod
    def floor(self, e):
        raise NotImplementedError

    @abstractmethod
    def ceiling(self, e):
        raise NotImplementedError

    @abstractmethod
    def higher(self, e):
        raise NotImplementedError

    @abstractmethod
    def poll_first(self):
        raise NotImplementedError

    @abstractmethod
    def poll_last(self):
        raise NotImplementedError

    @abstractmethod
    def iterator(self):
        raise NotImplementedError

    __iter__ = iterator

    @abstractmethod
    def descending_set(self):
        raise NotImplementedError

    @abstractmethod
    def descending_iterator(self):
        raise NotImplementedError

    __reversed__ = descending_iterator

    @abstractmethod
    def sub_set(self, from_element, to_element,
                from_inclusive=True, to_inclusive=False):
        raise NotImplementedError

    @abstractmethod
    def head_set(self, to_element, inclusive=False):
        raise NotImplementedError

    @abstractmethod
    def tail_set(self, from_element, inclusive=True):
        raise NotImplementedError

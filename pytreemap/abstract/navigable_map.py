#!/usr/bin/env python
"""A Python implementation of the Java NavigableMap interface.
"""
from abc import abstractmethod
from .sorted_map import SortedMap

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'
__version__ = '0.4'
__status__ = 'Alpha'


class NavigableMap(SortedMap):

    @abstractmethod
    def lower_entry(self, key):
        raise NotImplementedError

    @abstractmethod
    def lower_key(self, key):
        raise NotImplementedError

    @abstractmethod
    def floor_entry(self, key):
        raise NotImplementedError

    @abstractmethod
    def floor_key(self, key):
        raise NotImplementedError

    @abstractmethod
    def ceiling_entry(self, key):
        raise NotImplementedError

    @abstractmethod
    def ceiling_key(self, key):
        raise NotImplementedError

    @abstractmethod
    def higher_entry(self, key):
        raise NotImplementedError

    @abstractmethod
    def higher_key(self, key):
        raise NotImplementedError

    @abstractmethod
    def first_entry(self):
        raise NotImplementedError

    @abstractmethod
    def last_entry(self):
        raise NotImplementedError

    @abstractmethod
    def poll_first_entry(self):
        raise NotImplementedError

    @abstractmethod
    def poll_last_entry(self):
        raise NotImplementedError

    @abstractmethod
    def descending_map(self):
        raise NotImplementedError

    @abstractmethod
    def navigable_key_set(self):
        raise NotImplementedError

    @abstractmethod
    def descending_key_set(self):
        raise NotImplementedError

    @abstractmethod
    def sub_map(self, from_key, to_key,
                from_inclusive=True, to_inclusive=False):
        raise NotImplementedError

    @abstractmethod
    def head_map(self, to_key, inclusive=False):
        raise NotImplementedError

    @abstractmethod
    def tail_map(self, from_key, inclusive=True):
        raise NotImplementedError

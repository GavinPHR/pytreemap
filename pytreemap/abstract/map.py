#!/usr/bin/env python
"""A Python implementation of the Java Map interface.
"""
from abc import ABC, abstractmethod

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'
__version__ = '0.1'
__status__ = 'Alpha'


class Map(ABC):

    @abstractmethod
    def size(self):
        raise NotImplementedError

    __len__ = size

    @abstractmethod
    def is_empty(self):
        raise NotImplementedError

    @abstractmethod
    def contains_key(self, key):
        raise NotImplementedError

    __contains__ = contains_key

    @abstractmethod
    def contains_value(self, value):
        raise NotImplementedError

    @abstractmethod
    def get(self, key):
        raise NotImplementedError

    __getitem__ = get

    @abstractmethod
    def put(self, key, value):
        raise NotImplementedError

    __setitem__ = put

    @abstractmethod
    def remove(self, key):
        raise NotImplementedError

    __delitem__ = remove

    @abstractmethod
    def put_all(self, m):
        raise NotImplementedError

    @abstractmethod
    def clear(self):
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

    class Entry(ABC):

        @abstractmethod
        def get_key(self):
            raise NotImplementedError

        @abstractmethod
        def get_value(self):
            raise NotImplementedError

        @abstractmethod
        def set_value(self, value):
            raise NotImplementedError

        @abstractmethod
        def equals(self, o):
            raise NotImplementedError

        __eq__ = equals

        @abstractmethod
        def hash_code(self):
            raise NotImplementedError

        __hash__ = hash_code

    @abstractmethod
    def equals(self, o):
        raise NotImplementedError

    __eq__ = equals

    @abstractmethod
    def hash_code(self):
        raise NotImplementedError

    __hash__ = hash_code

#!/usr/bin/env python
"""A Python implementation of the Java Map interface.
"""
from abc import ABC, abstractmethod

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'
__version__ = '0.4'
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

    def get_or_default(self, key, default_value):
        v = self.get(key)
        if v is not None or self.contains_key(key):
            return v
        else:
            return default_value

    def for_each(self, action):
        if action is None:
            raise TypeError
        for entry in self.entry_set():
            try:
                k = entry.get_key()
                v = entry.get_value()
            except RuntimeError:
                raise RuntimeError
            action(k, v)

    def replace_all(self, function):
        if function is None:
            raise TypeError
        for entry in self.entry_set():
            try:
                k = entry.get_key()
                v = entry.get_value()
            except RuntimeError:
                raise RuntimeError
            v = function(k, v)
            try:
                entry.set_value(v)
            except RuntimeError:
                raise RuntimeError

    def put_if_absent(self, key, value):
        v = self.get(key)
        if v is None:
            v = self.put(key, value)
        return v

    def replace(self, key, value1, value2=None):
        cur_value = self.get(key)
        if value2 is None:
            if cur_value is not None or self.contains_key(key):
                cur_value = self.put(key, value1)
            return cur_value
        if (cur_value != value1 or
                (cur_value is None and not self.contains_key(key))):
            return False
        self.put(key, value2)
        return True

    def compute_if_absent(self, key, mapping_function):
        if mapping_function is None:
            raise TypeError
        v = self.get(key)
        if v is None:
            new_value = mapping_function(key)
            if new_value is not None:
                self.put(key, new_value)
                return new_value
        return v

    def compute_if_present(self, key, remapping_function):
        if remapping_function is None:
            raise TypeError
        old_value = self.get(key)
        if old_value is not None:
            new_value = remapping_function(key, old_value)
            if new_value is not None:
                self.put(key, new_value)
                return new_value
            else:
                self.remove(key)
                return None
        else:
            return None

    def compute(self, key, remapping_function):
        if remapping_function is None:
            raise TypeError
        old_value = self.get(key)
        new_value = remapping_function(key, old_value)
        if new_value is None:
            if old_value is not None or self.contains_key(key):
                self.remove(key)
                return None
            else:
                return None
        else:
            self.put(key, new_value)
            return new_value

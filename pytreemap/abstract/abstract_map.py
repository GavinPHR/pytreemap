#!/usr/bin/env python
"""A Python implementation of the Java AbstractMap interface.
"""
from abc import abstractmethod
from .map import Map

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'
__version__ = '0.4'
__status__ = 'Alpha'

class AbstractMap(Map):

    def __init__(self):
        self._key_set = None
        self._values = None

    def size(self):
        return self.entry_set().size()

    __len__ = size

    def is_empty(self):
        return self.size() == 0

    def contains_value(self, value):
        i = iter(self.entry_set())
        if value is None:
            for e in i:
                if e.get_value() is None:
                    return True
        else:
            for e in i:
                if value == e.get_value():
                    return True
        return False

    def contains_key(self, key):
        i = iter(self.entry_set())
        if key is None:
            for e in i:
                if e.get_key() is None:
                    return True
        else:
            for e in i:
                if key == e.get_key():
                    return True
        return False

    __contains__ = contains_key

    def get(self, key):
        i = iter(self.entry_set())
        if key is None:
            for e in i:
                if e.get_key() is None:
                    return e.get_value()
        else:
            for e in i:
                if key == e.get_key():
                    return e.get_value()
        return None

    __getitem__ = get

    def put(self, key, value):
        raise NotImplementedError

    __setitem__ = put

    def remove(self, key):
        i = iter(self.entry_set())
        correct_entry = None
        if key is None:
            for e in i:
                if e.get_key() is None:
                    correct_entry = e
                    break
        else:
            for e in i:
                if key == e.get_key():
                    correct_entry = e
                    break
        old_value = None
        if correct_entry is not None:
            old_value = correct_entry.get_value()
            i.remove()
        return old_value

    __delitem__ = remove

    def put_all(self, m):
        for e in m.entry_set():
            self.put(e.get_key(), e.get_value())

    def clear(self):
        self.entry_set().clear()

    def key_set(self):
        if self._key_set is None:

            from .abstract_set import AbstractSet
            class AnonAbstractSet(AbstractSet):

                def __init__(self, outer):
                    self.outer = outer

                from collections.abc import Iterator
                class AnonIterator(Iterator):

                    def __init__(self, outer):
                        self.i = iter(outer.entry_set())

                    def has_next(self):
                        return self.i.has_next()

                    def next(self):
                        return next(self.i).get_key()

                    __next__ = next

                    def remove(self):
                        self.i.remove()

                def iterator(self):
                    return self.AnonIterator(self.outer)

                __iter__ = iterator

                def size(self):
                    return self.outer.size()

                __len__ = size

                def is_empty(self):
                    return self.outer.is_empty()

                def clear(self):
                    self.outer.clear()

                def contains(self, k):
                    return self.outer.contains_key(k)

                __contains__ = contains

            self._key_set = AnonAbstractSet(self)
        return self._key_set

    def values(self):
        if self._values is None:

            from .abstract_collection import AbstractCollection
            class AnonAbstractCollection(AbstractCollection):

                def __init__(self, outer):
                    self.outer = outer

                from collections.abc import Iterator
                class AnonIterator(Iterator):

                    def __init__(self, outer):
                        self.i = outer.entry_set().iterator()

                    def has_next(self):
                        return self.i.has_next()

                    def next(self):
                        return self.i.next().get_value()

                    __next__ = next

                    def remove(self):
                        return self.i.remove()

                def iterator(self):
                    return self.AnonIterator(self.outer)

                __iter__ = iterator

                def size(self):
                    return self.outer.size()

                __len__ = size

                def is_empty(self):
                    return self.outer.is_empty()

                def clear(self):
                    self.outer.clear()

                def contains(self, k):
                    self.outer.contains_value(k)

                __contains__ = contains

                def equals(self, o):
                    raise NotImplementedError

                __eq__ = equals

                def hash_code(self):
                    raise NotImplementedError

                __hash__ = hash_code

            self._values = AnonAbstractCollection(self)
        return self._values

    @abstractmethod
    def entry_set(self):
        raise NotImplementedError

    def equals(self, o):
        if o is self:
            return True
        if not isinstance(o, Map):
            return False
        m = o
        if m.size() != self.size():
            return False
        try:
            i = iter(self.entry_set())
            for e in i:
                key = e.get_key()
                value = e.get_value()
                if value is None:
                    if not (m.get(key) is None and m.contains_key(key)):
                        return False
                else:
                    if value != m.get(key):
                        return False
        except TypeError:
            return False
        return True

    __eq__ = equals

    def hash_code(self):
        h = 0
        i = iter(self.entry_set())
        for e in i:
            h += hash(e)
        return h

    __hash__ = hash_code

    def to_string(self):
        i = iter(self.entry_set())
        s = ['{']
        for e in i:
            key = e.get_key()
            value = e.get_value()
            s.append('(this Map)' if key is self else str(key))
            s.append('=')
            s.append('(this Map)' if value is self else str(value))
            s.append(', ')
        if s[-1] == '{':
            s.append('}')
        else:
            s[-1] = '}'
        return "".join(s)

    __repr__ = __str__ = to_string

    class SimpleEntry(Map.Entry):

        # Using some arbitrary value as placeholder
        # because value can be None.
        def __init__(self, key_or_entry, value='~!@)(*&^'):
            if value == '~!@)(*&^':  # Assume an entry is passed.
                entry = key_or_entry
                self.key = entry.get_key()
                self.value = entry.get_value()
            else:
                key = key_or_entry
                self.key = key
                self.value = value

        def get_key(self):
            return self.key

        def get_value(self):
            return self.value

        def set_value(self, value):
            old_value = self.value
            self.value = value
            return old_value

        def equals(self, o):
            if not isinstance(o, Map.Entry):
                return False
            e = o
            return (self.key == e.get_key() and
                    self.value == e.get_value())

        __eq__ = equals

        def hash_code(self):
            return ((0 if self.key is None else hash(self.key)) ^
                    (0 if self.value is None else hash(self.value)))

        __hash__ = hash_code

        def to_string(self):
            return str(self.key) + '=' + str(self.value)

        __repr__ = __str__ = to_string

    class SimpleImmutableEntry(Map.Entry):

        def __init__(self, key_or_entry, value='~!@)(*&^'):
            if value == '~!@)(*&^':  # Assume an entry is passed.
                entry = key_or_entry
                self.key = entry.get_key()
                self.value = entry.get_value()
            else:
                key = key_or_entry
                self.key = key
                self.value = value

        def get_key(self):
            return self.key

        def get_value(self):
            return self.value

        def set_value(self, value):
            raise NotImplementedError

        def equals(self, o):
            if not isinstance(o, Map.Entry):
                return False
            e = o
            return (self.key == e.get_key() and
                    self.value == e.get_value())

        __eq__ = equals

        def hash_code(self):
            return ((0 if self.key is None else hash(self.key)) ^
                    (0 if self.value is None else hash(self.value)))

        __hash__ = hash_code

        def to_string(self):
            return str(self.key) + '=' + str(self.value)

        __repr__ = __str__ = to_string

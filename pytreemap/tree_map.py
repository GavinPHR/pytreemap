#!/usr/bin/env python
"""A Python implementation of the Java TreeMap.
"""
from .abstract.map import Map
from .abstract.abstract_map import AbstractMap
from .abstract.navigable_map import NavigableMap

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'
__version__ = '0.4'
__status__ = 'Alpha'


class TreeMap(NavigableMap, AbstractMap, Map):

    def __init__(self, comparator=None):
        """User can pass in a comparator function to allow key objects
        that do not implement the rich comparison methods.
        """
        self._root = None
        self._comparator = comparator
        self._size = 0
        self._mod_count = 0

        super().__init__()
        self._entry_set = None
        self._navigable_key_set = None
        self._descending_map = None

    def size(self):
        """Return the number of entries in the tree."""
        return self._size

    __len__ = size

    def contains_key(self, key):
        """Return True if this map contains a mapping
        for the specified key."""
        return self.get_entry(key) is not None

    __contains__ = contains_key

    def contains_value(self, value):
        """Returns true if at least 1 key is mapped to the value.
        The value must have implemented rich comparisons."""
        e = self.get_first_entry()
        while e is not None:
            if self.val_equals(value, e.value):
                return True
            e = self.successor(e)
        return False

    def get(self, key):
        """Return the value to which the specified key
        is mapped. Return None is no such mapping exists."""
        p = self.get_entry(key)
        return None if p is None else p.value

    def __getitem__(self, key):
        p = self.get_entry(key)
        if p is None:
            raise KeyError('key not found')
        return p.value

    def comparator(self):
        """Return the comparator function."""
        return self._comparator

    def first_key(self):
        """Return the first/smallest/left-most key."""
        return self.key(self.get_first_entry())

    def last_key(self):
        """Return the last/largest/right-most key."""
        return self.key(self.get_last_entry())

    def get_entry(self, key):
        """Return the entry for the key, or None if the key is not present."""
        if self._comparator is not None:
            return self.get_entry_using_comparator(key)
        if key is None:
            raise TypeError
        p = self._root
        while p is not None:
            if key < p.key:
                p = p.left
            elif key > p.key:
                p = p.right
            else:
                return p
        return None

    def get_entry_using_comparator(self, key):
        """Return the entry for the key, or None if the key is not present.
        This method is only called if a comparator function is supplied.
        """
        cpr = self._comparator
        if cpr is not None:
            p = self._root
            while p is not None:
                cmp = cpr(key, p.key)
                if cmp < 0:
                    p = p.left
                elif cmp > 0:
                    p = p.right
                else:
                    return p
        return None

    def get_ceiling_entry(self, key):
        """If key exists, return the corresponding entry.
        Otherwise return the entry with the least key greater than key.
        If no such entry exists, return None."""
        p = self._root
        while p is not None:
            cmp = self.compare(key, p.key)
            if cmp < 0:
                if p.left is not None:
                    p = p.left
                else:
                    return p
            elif cmp > 0:
                if p.right is not None:
                    p = p.right
                else:
                    parent = p.parent
                    ch = p
                    while parent is not None and ch is parent.right:
                        ch = parent
                        parent = parent.parent
                    return parent
            else:
                return p
        return None

    def get_floor_entry(self, key):
        """If key exists, return the corresponding entry.
        Otherwise return the entry with the greatest key less than key.
        If no such entry exists, return None."""
        p = self._root
        while p is not None:
            cmp = self.compare(key, p.key)
            if cmp > 0:
                if p.right is not None:
                    p = p.right
                else:
                    return p
            elif cmp < 0:
                if p.left is not None:
                    p = p.left
                else:
                    parent = p.parent
                    ch = p
                    while parent is not None and ch is parent.left:
                        ch = parent
                        parent = parent.parent
                    return parent
            else:
                return p
        return None

    def get_higher_entry(self, key):
        """Return entry with the least key greater than key.
        If no such entry exists, return None."""
        p = self._root
        while p is not None:
            cmp = self.compare(key, p.key)
            if cmp < 0:
                if p.left is not None:
                    p = p.left
                else:
                    return p
            else:
                if p.right is not None:
                    p = p.right
                else:
                    parent = p.parent
                    ch = p
                    while parent is not None and ch is parent.right:
                        ch = parent
                        parent = parent.parent
                    return parent
        return None

    def get_lower_entry(self, key):
        """Return entry with the greatest key less than key.
        If no such entry exists, return None."""
        p = self._root
        while p is not None:
            cmp = self.compare(key, p.key)
            if cmp > 0:
                if p.right is not None:
                    p = p.right
                else:
                    return p
            else:
                if p.left is not None:
                    p = p.left
                else:
                    parent = p.parent
                    ch = p
                    while parent is not None and ch is parent.left:
                        ch = parent
                        parent = parent.parent
                    return parent
        return None

    def put(self, key, value):
        """Associates the key with the value.
        If the key already exists, the old value is replaced."""
        t = self._root
        if t is None:
            self.compare(key, key)  # Type/None check
            self._root = self.Entry(key, value, None)
            self._size = 1
            self._mod_count += 1
            return None
        cmp = None
        parent = None
        cpr = self._comparator
        # Split compare paths between comparator function
        # and objects that implement rich comparisons.
        if cpr is not None:
            while True:
                parent = t
                cmp = cpr(key, t.key)
                if cmp < 0:
                    t = t.left
                elif cmp > 0:
                    t = t.right
                else:
                    return t.set_value(value)
                if t is None:
                    break
        else:
            if key is None:
                raise TypeError
            while True:
                parent = t
                if key < t.key:
                    cmp = -1
                    t = t.left
                elif key > t.key:
                    cmp = 1
                    t = t.right
                else:
                    return t.set_value(value)
                if t is None:
                    break
        e = self.Entry(key, value, parent)
        if cmp < 0:
            parent.left = e
        else:
            parent.right = e
        self.fix_after_insertion(e)
        self._size += 1
        self._mod_count += 1
        return None

    __setitem__ = put

    def remove(self, key):
        """Remove the entry with the key.
        Return the value."""
        p = self.get_entry(key)
        if p is None:
            return None
        old_value = p.value
        self.delete_entry(p)
        return old_value

    def __delitem__(self, key):
        p = self.get_entry(key)
        if p is None:
            raise KeyError('key not found')
        self.delete_entry(p)

    def clear(self):
        """Remove all entries."""
        self._mod_count += 1
        self._size = 0
        self._root = None

    """The NavigableMap API."""

    def first_entry(self):
        return self.export_entry(self.get_first_entry())

    def last_entry(self):
        return self.export_entry(self.get_last_entry())

    def poll_first_entry(self):
        p = self.get_first_entry()
        result = self.export_entry(p)
        if p is not None:
            self.delete_entry(p)
        return result

    def poll_last_entry(self):
        p = self.get_last_entry()
        result = self.export_entry(p)
        if p is not None:
            self.delete_entry(p)
        return result

    def lower_entry(self, key):
        return self.export_entry(self.get_lower_entry(key))

    def lower_key(self, key):
        return self.key_or_none(self.get_lower_entry(key))

    def floor_entry(self, key):
        return self.export_entry(self.get_floor_entry(key))

    def floor_key(self, key):
        return self.key_or_none(self.get_floor_entry(key))

    def ceiling_entry(self, key):
        return self.export_entry(self.get_ceiling_entry(key))

    def ceiling_key(self, key):
        return self.key_or_none(self.get_ceiling_entry(key))

    def higher_entry(self, key):
        return self.export_entry(self.get_higher_entry(key))

    def higher_key(self, key):
        return self.key_or_none(self.get_higher_entry(key))

    def key_set(self):
        return self.navigable_key_set()

    def navigable_key_set(self):
        if self._navigable_key_set is None:
            self._navigable_key_set = self.KeySet(self)
        return self._navigable_key_set

    def descending_key_set(self):
        return self.descending_map().navigable_key_set()

    def values(self):
        if self._values is None:
            self._values = self.Values(self)
        return self._values

    def entry_set(self):
        if self._entry_set is None:
            self._entry_set = self.EntrySet(self)
        return self._entry_set

    def descending_map(self):
        if self._descending_map is None:
            self._descending_map = self.DescendingSubMap(self,
                                                         True, None, True,
                                                         True, None, True)
        return self._descending_map

    def sub_map(self, from_key, to_key,
                from_inclusive=True, to_inclusive=False):
        return self.AscendingSubMap(self,
                                    False, from_key, from_inclusive,
                                    False, to_key, to_inclusive)

    def head_map(self, to_key, inclusive=False):
        return self.AscendingSubMap(self,
                                    True, None, True,
                                    False, to_key, inclusive)

    def tail_map(self, from_key, inclusive=True):
        return self.AscendingSubMap(self,
                                    False, from_key, inclusive,
                                    True, None, True)

    from .tree_map_inner_class.values import Values
    from .tree_map_inner_class.entry_set import EntrySet

    def key_iterator(self):
        return self.KeyIterator(self.get_first_entry(), self)

    __iter__ = key_iterator

    def descending_key_iterator(self):
        return self.DescendingKeyIterator(self.get_last_entry(), self)

    __reversed__ = descending_key_iterator

    from .tree_map_inner_class.key_set import KeySet
    from .tree_map_inner_class.private_entry_iterator \
        import PrivateEntryIterator
    from .tree_map_inner_class.entry_iterator import EntryIterator
    from .tree_map_inner_class.value_iterator import ValueIterator
    from .tree_map_inner_class.key_iterator import KeyIterator
    from .tree_map_inner_class.descending_key_iterator \
        import DescendingKeyIterator

    def compare(self, k1, k2):
        """Compare two keys, using the comparator function if supplied"""
        if self._comparator is not None:
            return self._comparator(k1, k2)
        if k1 < k2:
            return -1
        elif k1 > k2:
            return 1
        else:
            return 0

    @staticmethod
    def val_equals(o1, o2):
        """Compare two objects equality.
        o1 and o2 should implement rich comparison methods.
        o1 and o2 can also both be None."""
        return o2 is None if o1 is None else o1 == o2

    @staticmethod
    def export_entry(e):
        return None if e is None else AbstractMap.SimpleImmutableEntry(e)

    @staticmethod
    def key_or_none(e):
        """Return the entry's key, return None if entry is None."""
        return None if e is None else e.key

    @staticmethod
    def key(e):
        """Return the key of an entry.
        Raise exception if entry is None."""
        if e is None:
            raise KeyError('key not found')
        return e.key

    from .tree_map_inner_class.navigable_sub_map import NavigableSubMap
    from .tree_map_inner_class.ascending_sub_map import AscendingSubMap
    from .tree_map_inner_class.descending_sub_map import DescendingSubMap

    """Constants for red-black tree"""
    RED = False
    BLACK = True

    from .tree_map_inner_class.entry import Entry

    def get_first_entry(self):
        """Return the first/left-most/smallest entry."""
        p = self._root
        if p is not None:
            while p.left is not None:
                p = p.left
        return p

    def get_last_entry(self):
        """Return the last/right-most/largest entry."""
        p = self._root
        if p is not None:
            while p.right is not None:
                p = p.right
        return p

    @staticmethod
    def successor(t):
        """The successor is the closest larger entry.
        Return None if no successor exists."""
        if t is None:
            return None
        # If right child exists, then we should go
        # right and then keep going left.
        elif t.right is not None:
            p = t.right
            while p.left is not None:
                p = p.left
            return p
        # Otherwise we should go up until a node is
        # a left child of another node.
        else:
            p = t.parent
            ch = t
            while p is not None and ch is p.right:
                ch = p
                p = p.parent
            return p

    @staticmethod
    def predecessor(t):
        """The predecessor is the closest smaller entry.
        Return None if no predecessor exists."""
        if t is None:
            return None
        # If left child exists, then we should go
        # left and then keep going right.
        elif t.left is not None:
            p = t.left
            while p.right is not None:
                p = p.right
            return p
        # Otherwise we should go up until a node is
        # a right child of another node.
        else:
            p = t.parent
            ch = t
            while p is not None and ch is p.left:
                ch = p
                p = p.parent
            return p

    """Balancing operations."""

    @staticmethod
    def color_of(p):
        return TreeMap.BLACK if p is None else p.color

    @staticmethod
    def parent_of(p):
        return None if p is None else p.parent

    @staticmethod
    def set_color(p, c):
        if p is not None:
            p.color = c

    @staticmethod
    def left_of(p):
        return None if p is None else p.left

    @staticmethod
    def right_of(p):
        return None if p is None else p.right

    def rotate_left(self, p):
        """  |                        |
         ____p____      ===>      ____r____
        a       __r__          __p__       c
               b     c        a     b
        """
        if p is not None:
            r = p.right
            p.right = r.left
            if r.left is not None:
                r.left.parent = p
            r.parent = p.parent
            if p.parent is None:
                self._root = r
            elif p.parent.left is p:
                p.parent.left = r
            else:
                p.parent.right = r
            r.left = p
            p.parent = r

    def rotate_right(self, p):
        """     |                        |
            ____p____      ===>      ____l____
         __l__       c              a       __p__
        a     b                            b     c
        """
        if p is not None:
            l = p.left
            p.left = l.right
            if l.right is not None:
                l.right.parent = p
            l.parent = p.parent
            if p.parent is None:
                self._root = l
            elif p.parent.right is p:
                p.parent.right = l
            else:
                p.parent.left = l
            l.right = p
            p.parent = l

    def fix_after_insertion(self, x):
        # For convenience, reduce the amount of self.
        RED, BLACK = TreeMap.RED, TreeMap.BLACK
        left_of, right_of = self.left_of, self.right_of
        parent_of, set_color = self.parent_of, self.set_color

        x.color = RED
        while (x is not None and
               x is not self._root and
               x.parent.color == RED):
            if parent_of(x) is left_of(parent_of(parent_of(x))):
                y = right_of(parent_of(parent_of(x)))
                if self.color_of(y) == RED:
                    set_color(parent_of(x), BLACK)
                    set_color(y, BLACK)
                    set_color(parent_of(parent_of(x)), RED)
                    x = parent_of(parent_of(x))
                else:
                    if x is right_of(parent_of(x)):
                        x = parent_of(x)
                        self.rotate_left(x)
                    set_color(parent_of(x), BLACK)
                    set_color(parent_of(parent_of(x)), RED)
                    self.rotate_right(parent_of(parent_of(x)))
            else:
                y = left_of(parent_of(parent_of(x)))
                if self.color_of(y) == RED:
                    set_color(parent_of(x), BLACK)
                    set_color(y, BLACK)
                    set_color(parent_of(parent_of(x)), RED)
                    x = parent_of(parent_of(x))
                else:
                    if x is left_of(parent_of(x)):
                        x = parent_of(x)
                        self.rotate_right(x)
                    set_color(parent_of(x), BLACK)
                    set_color(parent_of(parent_of(x)), RED)
                    self.rotate_left(parent_of(parent_of(x)))
        self._root.color = BLACK

    def delete_entry(self, p):
        self._mod_count += 1
        self._size -= 1
        if p.left is not None and p.right is not None:
            s = self.successor(p)
            p.key = s.key
            p.value = s.value
            p = s
        replacement = p.left if p.left is not None else p.right
        if replacement is not None:
            replacement.parent = p.parent
            if p.parent is None:
                self._root = replacement
            elif p is p.parent.left:
                p.parent.left = replacement
            else:
                p.parent.right = replacement
            p.left = p.right = p.parent = None
            if p.color == TreeMap.BLACK:
                self.fix_after_deletion(replacement)
        elif p.parent is None:
            self._root = None
        else:
            if p.color == TreeMap.BLACK:
                self.fix_after_deletion(p)
            if p.parent is not None:
                if p is p.parent.left:
                    p.parent.left = None
                elif p is p.parent.right:
                    p.parent.right = None
                p.parent = None

    def fix_after_deletion(self, x):
        # For convenience, reduce the amount of self.
        RED, BLACK = TreeMap.RED, TreeMap.BLACK
        left_of, right_of = self.left_of, self.right_of
        parent_of, set_color = self.parent_of, self.set_color
        color_of = self.color_of

        while x is not self._root and color_of(x) == BLACK:
            if x is left_of(parent_of(x)):
                sib = right_of(parent_of(x))
                if color_of(sib) == RED:
                    set_color(sib, BLACK)
                    set_color(parent_of(x), RED)
                    self.rotate_left(parent_of(x))
                    sib = right_of(parent_of(x))
                if (color_of(left_of(sib)) == BLACK and
                        color_of(right_of(sib)) == BLACK):
                    x = parent_of(x)
                else:
                    if color_of(right_of(sib)) == BLACK:
                        set_color(left_of(sib), BLACK)
                        set_color(sib, RED)
                        self.rotate_right(sib)
                        sib = right_of(parent_of(x))
                    set_color(sib, color_of(parent_of(x)))
                    set_color(parent_of(x), BLACK)
                    set_color(right_of(sib), BLACK)
                    self.rotate_left(parent_of(x))
                    x = self._root
            else:
                sib = left_of(parent_of(x))
                if color_of(sib) == RED:
                    set_color(sib, BLACK)
                    set_color(parent_of(x), RED)
                    self.rotate_right(parent_of(x))
                    sib = left_of(parent_of(x))
                if (color_of(right_of(sib)) == BLACK and
                        color_of(left_of(sib)) == BLACK):
                    set_color(sib, RED)
                    x = parent_of(x)
                else:
                    if color_of(left_of(sib)) == BLACK:
                        set_color(right_of(sib), BLACK)
                        set_color(sib, RED)
                        self.rotate_left(sib)
                        sib = left_of(parent_of(x))
                    set_color(sib, color_of(parent_of(x)))
                    set_color(parent_of(x), BLACK)
                    set_color(left_of(sib), BLACK)
                    self.rotate_right(parent_of(x))
                    x = self._root
        set_color(x, BLACK)

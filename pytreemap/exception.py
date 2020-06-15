#!/usr/bin/env python
"""Exceptions used in this package.
"""

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'
__version__ = '0.3'
__status__ = 'Alpha'


class IllegalStateError(RuntimeError):
    pass


class ConcurrentModificationError(RuntimeError):
    pass


class UnsupportedOperationError(RuntimeError):
    pass

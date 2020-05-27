#!/usr/bin/env python
"""Test the default methods from the Java Map interface.
Obviously only TreeMap is tested.
"""

import pytest
from pytreemap import TreeMap

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'

class TestDefaults:

    # Set up key enums.
    from enum import IntEnum
    # noinspection
    IntegerEnum = IntEnum('IntegerEnum',
                       'e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, '
                       'e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, '
                       'e20, e21, e22, e23, e24, e25, e26, e27, e28, e29, '
                       'e30, e31, e32, e33, e34, e35, e36, e37, e38, e39, '
                       'e40, e41, e42, e43, e44, e45, e46, e47, e48, e49, '
                       'e50, e51, e52, e53, e54, e55, e56, e57, e58, e59, '
                       'e60, e61, e62, e63, e64, e65, e66, e67, e68, e69, '
                       'e70, e71, e72, e73, e74, e75, e76, e77, e78, e79, '
                       'e80, e81, e82, e83, e84, e85, e86, e87, e88, e89, '
                       'e90, e91, e92, e93, e94, e95, e96, e97, e98, e99, '
                       'EXTRA_KEY')
    TEST_SIZE = len(IntegerEnum) - 1

    # Init key values
    KEYS = [0] * TEST_SIZE
    VALUES = [0] * TEST_SIZE
    keys = list(IntegerEnum)
    for each in range(TEST_SIZE):
        KEYS[each] = keys[each]
        VALUES[each] = str(each)

    FIRST_KEY = KEYS[0]
    FIRST_VALUE = VALUES[0]
    EXTRA_KEY = IntegerEnum.EXTRA_KEY
    EXTRA_VALUE = str(TEST_SIZE)

    @pytest.fixture
    def map(self):
        """Read/Write No None Keys Map (With None Value).
        This corresponds to the TreeMap part of the rwMapProvider in Java."""
        tm = TreeMap()
        for each in range(self.TEST_SIZE):
            key = self.KEYS[each]
            value = None if each == 0 else self.VALUES[each]
            tm.put(key, value)
        return tm

    def test_put_if_absent(self, map):
        KEYS, VALUES = self.KEYS, self.VALUES
        assert map.contains_key(KEYS[1])
        expected = map.get(KEYS[1])
        assert (expected == None) or (expected == VALUES[1])
        # assert map.put_if_absent(KEYS[1], )
        """
        To be cont.
        """

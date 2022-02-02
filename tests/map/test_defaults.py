#!/usr/bin/env python
import pytest
from pytreemap import TreeMap

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'


class TestDefaults:

    # Set up key enums.
    from enum import IntEnum
    # IntEnum starts from 1 instead of 0
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
    def make_map(self):
        """rw=true keys=non_null map.
        Specify if null_values wanted below."""
        def make(null_values):
            tm = TreeMap()
            for each in range(self.TEST_SIZE):
                key = self.KEYS[each]
                value = ((None if each == 0 else self.VALUES[each])
                         if null_values else self.VALUES[each])
                tm.put(key, value)
            return tm
        return make

    """rw=all keys=all values=all"""

    def test_get_or_default(self, make_map):
        KEYS, VALUES = self.KEYS, self.VALUES
        EXTRA_KEY, EXTRA_VALUE = self.EXTRA_KEY, self.EXTRA_VALUE
        map = make_map(True)
        assert map.contains_key(KEYS[1])
        assert map.get(KEYS[1]) is map.get_or_default(KEYS[1], EXTRA_VALUE)
        assert not map.contains_key(EXTRA_KEY)
        assert map.get_or_default(EXTRA_KEY, EXTRA_VALUE) is EXTRA_VALUE
        assert map.get_or_default(EXTRA_KEY, None) is None

    def test_for_each(self, make_map):
        map = make_map(True)
        KEYS = self.KEYS
        EACH_KEY = [None]*map.size()
        def f(k, v):
            idx = 0 if k is None else int(k)-1
            assert EACH_KEY[idx] is None
            EACH_KEY[idx] = KEYS[0] if idx == 0 else k
            assert v is map.get(k)
        map.for_each(f)
        assert KEYS == EACH_KEY

    """rw=true keys=all values=all"""

    def test_put_if_absent(self, make_map):
        KEYS, VALUES = self.KEYS, self.VALUES
        EXTRA_KEY, EXTRA_VALUE = self.EXTRA_KEY, self.EXTRA_VALUE
        map = make_map(True)
        assert map.contains_key(KEYS[1])
        expected = map.get(KEYS[1])
        assert expected is None or expected is VALUES[1]
        assert map.put_if_absent(KEYS[1], EXTRA_VALUE) is expected
        assert map.get(KEYS[1]) is expected

        assert not map.contains_key(EXTRA_KEY)
        assert map.put_if_absent(EXTRA_KEY, EXTRA_VALUE) is None
        assert map.get(EXTRA_KEY) is EXTRA_VALUE
        assert map.put_if_absent(EXTRA_KEY, VALUES[2]) is EXTRA_VALUE
        assert map.get(EXTRA_KEY) is EXTRA_VALUE

    def test_replace_all(self, make_map):
        map = make_map(True)
        KEYS = self.KEYS
        EACH_KEY = [None] * map.size()
        EACH_REPLACE = set()
        def f(k, v):
            idx = 0 if k is None else int(k)-1
            assert EACH_KEY[idx] is None
            EACH_KEY[idx] = KEYS[0] if idx == 0 else k
            assert v is map.get(k)
            replacement = str(v)  + ' replaced'
            EACH_REPLACE.add(replacement)
            return replacement
        map.replace_all(f)
        assert KEYS == EACH_KEY
        assert map.values().size() == len(EACH_REPLACE)
        assert EACH_REPLACE.issuperset(map.values())
        assert map.values().contains_all(EACH_REPLACE)

    def test_remove(self, make_map):
        KEYS, VALUES = self.KEYS, self.VALUES
        EXTRA_KEY, EXTRA_VALUE = self.EXTRA_KEY, self.EXTRA_VALUE
        map = make_map(True)
        assert map.contains_key(KEYS[1])
        expected = map.get(KEYS[1])
        assert expected is None or expected is VALUES[1]
        assert map.remove(KEYS[1])
        assert map.get(KEYS[1]) is None
        assert not map.remove(KEYS[1])
        assert not map.contains_key(EXTRA_KEY)
        assert not map.remove(EXTRA_KEY)

    def test_replace_kv(self, make_map):
        KEYS, VALUES = self.KEYS, self.VALUES
        EXTRA_KEY, EXTRA_VALUE = self.EXTRA_KEY, self.EXTRA_VALUE
        map = make_map(True)
        assert map.contains_key(KEYS[1])
        expected = map.get(KEYS[1])
        assert expected is None or expected is VALUES[1]
        assert map.replace(KEYS[1], EXTRA_VALUE) is expected
        assert map.get(KEYS[1]) is EXTRA_VALUE

        assert not map.contains_key(EXTRA_KEY)
        assert map.replace(EXTRA_KEY, EXTRA_VALUE) is None
        assert not map.contains_key(EXTRA_KEY)
        assert map.get(EXTRA_KEY) is None
        assert map.put(EXTRA_KEY, EXTRA_VALUE) is None
        assert map.get(EXTRA_KEY) is EXTRA_VALUE
        assert map.replace(EXTRA_KEY, expected) is EXTRA_VALUE
        assert map.get(EXTRA_KEY) is expected

    def test_replace_kvv(self, make_map):
        KEYS, VALUES = self.KEYS, self.VALUES
        EXTRA_KEY, EXTRA_VALUE = self.EXTRA_KEY, self.EXTRA_VALUE
        map = make_map(True)
        assert map.contains_key(KEYS[1])
        expected = map.get(KEYS[1])
        assert expected is None or expected is VALUES[1]
        assert not map.replace(KEYS[1], EXTRA_VALUE, EXTRA_VALUE)
        assert map.get(KEYS[1]) is expected
        assert map.replace(KEYS[1], expected, EXTRA_VALUE)
        assert map.get(KEYS[1]) is EXTRA_VALUE
        assert map.replace(KEYS[1], EXTRA_VALUE, EXTRA_VALUE)
        assert map.get(KEYS[1]) is EXTRA_VALUE

        assert not map.contains_key(EXTRA_KEY)
        assert not map.replace(EXTRA_KEY, EXTRA_VALUE, EXTRA_VALUE)
        assert not map.contains_key(EXTRA_KEY)
        assert map.get(EXTRA_KEY) is None
        assert map.put(EXTRA_KEY, EXTRA_VALUE) is None
        assert map.contains_key(EXTRA_KEY)
        assert map.get(EXTRA_KEY) is EXTRA_VALUE
        assert map.replace(EXTRA_KEY, EXTRA_VALUE, EXTRA_VALUE)
        assert map.get(EXTRA_KEY) is EXTRA_VALUE

    def test_compute_if_absent(self, make_map):
        KEYS, VALUES = self.KEYS, self.VALUES
        EXTRA_KEY, EXTRA_VALUE = self.EXTRA_KEY, self.EXTRA_VALUE
        map = make_map(True)
        assert map.contains_key(KEYS[1])
        expected = map.get(KEYS[1])
        assert expected is None or expected is VALUES[1]
        expected = EXTRA_VALUE if expected is None else expected
        assert map.compute_if_absent(KEYS[1], lambda k: EXTRA_VALUE) is expected
        assert map.get(KEYS[1]) is expected

        assert not map.contains_key(EXTRA_KEY)
        assert map.compute_if_absent(EXTRA_KEY, lambda k: None) is None
        assert not map.contains_key(EXTRA_KEY)
        assert map.compute_if_absent(EXTRA_KEY, lambda k: EXTRA_VALUE) is EXTRA_VALUE
        assert map.get(EXTRA_KEY) is EXTRA_VALUE

    def test_compute_if_absent_null_function(self, make_map):
        KEYS = self.KEYS
        map = make_map(True)
        with pytest.raises(TypeError):
            map.compute_if_absent(KEYS[1], None)

    def test_compute_if_present(self, make_map):
        KEYS, VALUES = self.KEYS, self.VALUES
        EXTRA_KEY, EXTRA_VALUE = self.EXTRA_KEY, self.EXTRA_VALUE
        map = make_map(True)
        assert map.contains_key(KEYS[1])
        value = map.get(KEYS[1])
        assert value is None or value is VALUES[1]
        expected = None if value is None else EXTRA_VALUE
        def f(k, v):
            assert v is value
            return EXTRA_VALUE
        assert map.compute_if_present(KEYS[1], f) is expected
        assert map.get(KEYS[1]) is expected

        assert not map.contains_key(EXTRA_KEY)
        def f(k, v):
            pytest.fail()
            return EXTRA_VALUE
        assert map.compute_if_present(EXTRA_KEY, f) is None
        assert not map.contains_key(EXTRA_KEY)
        assert map.get(EXTRA_KEY) is None

    def test_compute_if_present_null_function(self, make_map):
        KEYS = self.KEYS
        map = make_map(True)
        with pytest.raises(TypeError):
            map.compute_if_present(KEYS[1], None)

    def test_compute(self, make_map):
        KEYS, VALUES = self.KEYS, self.VALUES
        EXTRA_KEY, EXTRA_VALUE = self.EXTRA_KEY, self.EXTRA_VALUE
        map = make_map(True)
        assert map.contains_key(KEYS[1])
        value = map.get(KEYS[1])
        assert value is None or value is VALUES[1]
        def f(k, v):
            assert k is KEYS[1]
            assert v is value
            return EXTRA_VALUE
        assert map.compute(KEYS[1], f) is EXTRA_VALUE
        assert map.get(KEYS[1]) is EXTRA_VALUE
        def f(k, v):
            assert v is EXTRA_VALUE
            return None
        assert map.compute(KEYS[1], f) is None
        assert not map.contains_key(KEYS[1])

        assert not map.contains_key(EXTRA_KEY)
        def f(k, v):
            assert v is None
            return EXTRA_VALUE
        assert map.compute(EXTRA_KEY, f) is EXTRA_VALUE
        assert map.contains_key(EXTRA_KEY)
        assert map.get(EXTRA_KEY) is EXTRA_VALUE

    def test_compute_null_function(self, make_map):
        KEYS = self.KEYS
        map = make_map(True)
        with pytest.raises(TypeError):
            map.compute(KEYS[1], None)

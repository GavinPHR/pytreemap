#!/usr/bin/env python
"""moat = mother of all test"""
import pytest
from pytreemap import TreeMap

__author__ = 'Haoran Peng'
__email__ = 'gavinsweden@gmail.com'
__license__ = 'GPL-2.0'


class TestMOAT:

    def test_main(self):
        m = TreeMap()
        self.test_navigable_map_removers(m)
        self.test_navigable_map(m)
        self.test_navigable_map(m.head_map(6, False))
        self.test_navigable_map(m.head_map(5, True))
        self.test_navigable_map(m.tail_map(0, False))
        self.test_navigable_map(m.tail_map(1, True))
        self.test_navigable_map(m.sub_map(1, 6, True, False))
        self.test_navigable_map(m.sub_map(0, 5, False, True))

        self.check_functional_invariants(m)

        m.clear()

        assert m.put(3333, 77777) is None
        assert m.put(9134, 74982) is None
        assert m.get(9134) == 74982
        assert m.put(9134, 1382) == 74982
        assert m.get(9134) == 1382
        assert m.size() == 2
        self.check_functional_invariants(m)

    @pytest.mark.skip('called in main')
    def test_navigable_map_removers(self, m):
        views = [m,
                 m.head_map(99, True),
                 m.tail_map(-99, False),
                 m.sub_map(-99, 99, True, False)]

        def f1(m, k, v): assert m.remove(k) == v
        def f2(m, k, v): assert m.descending_map().remove(k) == v
        def f3(m, k, v): assert m.descending_map().head_map(-86, False).remove(k) == v
        def f4(m, k, v): assert m.descending_map().tail_map(86, True).remove(k) == v
        def f5(m, k, v): assert m.head_map(86, True).remove(k) == v
        def f6(m, k, v): assert m.tail_map(-86, True).remove(k) == v
        def f7(m, k, v): assert m.sub_map(-86, 86, False, True).remove(k) == v
        def f8(m, k, v): assert m.key_set().remove(k)
        def f9(m, k, v): assert m.navigable_key_set().head_set(86, True).remove(k)
        def f10(m, k, v): assert m.navigable_key_set().tail_set(-86, False).remove(k)
        def f11(m, k, v): assert m.navigable_key_set().sub_set(-86, 86, True, False).remove(k)
        def f12(m, k, v): assert m.descending_key_set().head_set(-86, False).remove(k)
        def f13(m, k, v): assert m.descending_key_set().tail_set(86, True).remove(k)
        def f14(m, k, v): assert m.descending_key_set().sub_set(86, -86, True, False).remove(k)
        removers = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14]

        for view in views:
            for remover in removers:
                m.clear()
                self.equal_maps(m, TreeMap())
                assert m.put(1, 2) is None
                assert m.size() == 1
                remover(view, 1, 2)
                self.equal_maps(m, TreeMap())

    @staticmethod
    def equal_maps(m1, m2):
        assert m1 == m2
        assert m2 == m1
        assert m1.size() == m2.size()
        assert m1.is_empty() == m2.is_empty()
        assert m1.to_string() == m2.to_string()
        assert m1.entry_set().to_list() == m2.entry_set().to_list()

    @pytest.mark.skip('called in main')
    def test_navigable_map(self, m):
        m.clear()
        self.check_navigable_map_keys(m, 1, None, None, None, None)

        assert m.put(1, 2) is None
        assert m.put(3, 4) is None
        assert m.put(5, 9) is None

        assert m.put(1, 2) == 2
        assert m.put(3, 4) == 4
        assert m.put(5, 6) == 9

        self.check_navigable_map_keys(m, 0, None, None,    1,    1)
        self.check_navigable_map_keys(m, 1, None,    1,    1,    3)
        self.check_navigable_map_keys(m, 2,    1,    1,    3,    3)
        self.check_navigable_map_keys(m, 3,    1,    3,    3,    5)
        self.check_navigable_map_keys(m, 5,    3,    5,    5, None)
        self.check_navigable_map_keys(m, 6,    5,    5, None, None)

        for it in iter(m.descending_key_set()), reversed(m.navigable_key_set()):
            assert next(it) == 5
            assert next(it) == 3
            assert next(it) == 1
            assert not it.has_next()
            with pytest.raises(StopIteration):
                next(it)

        it = iter(m.descending_map().entry_set())
        assert it.has_next()
        assert next(it).get_key() == 5
        assert it.has_next()
        assert next(it).get_key() == 3
        assert it.has_next()
        assert next(it).get_key() == 1
        assert not it.has_next()
        with pytest.raises(StopIteration):
            next(it)

        self.prep_map_for_desc_itr_tests(m)
        self.check_desc_itr_rm_first(m.key_set(), m.navigable_key_set().descending_iterator())
        self.prep_map_for_desc_itr_tests(m)
        self.check_desc_itr_rm_mid(m.key_set(), m.navigable_key_set().descending_iterator())
        self.prep_map_for_desc_itr_tests(m)
        self.check_desc_itr_rm_last(m.key_set(), m.navigable_key_set().descending_iterator())

        self.prep_map_for_desc_itr_tests(m)
        self.check_desc_itr_rm_first(m.key_set(), m.descending_map().key_set().iterator())
        self.prep_map_for_desc_itr_tests(m)
        self.check_desc_itr_rm_mid(m.key_set(), m.descending_map().key_set().iterator())
        self.prep_map_for_desc_itr_tests(m)
        self.check_desc_itr_rm_last(m.key_set(), m.descending_map().key_set().iterator())

        self.prep_map_for_desc_itr_tests(m)
        self.check_desc_itr_rm_first(m.key_set(), m.descending_key_set().iterator())
        self.prep_map_for_desc_itr_tests(m)
        self.check_desc_itr_rm_mid(m.key_set(), m.descending_key_set().iterator())
        self.prep_map_for_desc_itr_tests(m)
        self.check_desc_itr_rm_last(m.key_set(), m.descending_key_set().iterator())

        self.prep_map_for_desc_itr_tests(m)
        self.check_desc_itr_rm_first(m.values(), m.descending_map().values().iterator())
        self.prep_map_for_desc_itr_tests(m)
        self.check_desc_itr_rm_mid(m.values(), m.descending_map().values().iterator())
        self.prep_map_for_desc_itr_tests(m)
        self.check_desc_itr_rm_last(m.values(), m.descending_map().values().iterator())

        self.prep_map_for_desc_itr_tests(m)
        self.check_desc_itr_rm_first(m.entry_set(), m.descending_map().entry_set().iterator())
        self.prep_map_for_desc_itr_tests(m)
        self.check_desc_itr_rm_mid(m.entry_set(), m.descending_map().entry_set().iterator())
        self.prep_map_for_desc_itr_tests(m)
        self.check_desc_itr_rm_last(m.entry_set(), m.descending_map().entry_set().iterator())

    @staticmethod
    def check_navigable_map_keys(m, i, lower, floor, ceiling, higher):
        assert m.lower_key(i) == lower
        assert m.floor_key(i) == floor
        assert m.ceiling_key(i) == ceiling
        assert m.higher_key(i) == higher

    @staticmethod
    def prep_map_for_desc_itr_tests(m):
        m.clear()
        assert m.put(1, 2) is None
        assert m.put(3, 4) is None
        assert m.put(5, 9) is None

    @staticmethod
    def check_desc_itr_rm_first(asc_coll, desc_itr):
        expected = asc_coll.to_list()
        idx = len(expected) - 1
        assert next(desc_itr) == expected[idx]
        idx -= 1
        desc_itr.remove()
        while idx >= 0 and desc_itr.has_next():
            assert next(desc_itr) == expected[idx]
            idx -= 1
        assert not desc_itr.has_next()
        assert idx == -1

    @staticmethod
    def check_desc_itr_rm_mid(asc_coll, desc_itr):
        expected = asc_coll.to_list()
        idx = len(expected) - 1
        while idx >= len(expected) // 2:
            assert next(desc_itr) == expected[idx]
            idx -= 1
        desc_itr.remove()
        while idx >= 0 and desc_itr.has_next():
            assert next(desc_itr) == expected[idx]
            idx -= 1
        assert not desc_itr.has_next()
        assert idx == -1

    @staticmethod
    def check_desc_itr_rm_last(asc_coll, desc_itr):
        expected = asc_coll.to_list()
        idx = len(expected) - 1
        while idx >= 0 and desc_itr.has_next():
            assert next(desc_itr) == expected[idx]
            idx -= 1
        assert not desc_itr.has_next()
        assert idx == -1
        desc_itr.remove()
        assert not asc_coll.contains(expected[0])

    def check_functional_invariants(self, m):
        assert m.key_set().size() == m.entry_set().size()
        assert m.key_set().size() == m.size()
        self.check_functional_invariants_(m.key_set())
        self.check_functional_invariants_(m.values())
        assert m.size() != (0 ^ int(m.is_empty()))

    def check_functional_invariants_(self, c):
        self.check_contains_self(c)
        self.check_contains_empty(c)
        assert c.size() != (0 ^ int(c.is_empty()))
        size = 0
        for i in c:
            size += 1
        assert c.size() == size
        assert len(c.to_list()) == c.size()
        assert c == c

    @staticmethod
    def check_contains_self(c):
        assert c.contains_all(c)
        assert c.contains_all(c.to_list())

    @staticmethod
    def check_contains_empty(c):
        assert c.contains_all([])

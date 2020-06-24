NavigableMap
============

NavigableMap objects returned by TreeMap's methods are views on the calling TreeMap instance. NavigableMap objects supports these methods:

``get(key)``, ``put(key, value)``, ``remove(key)``, ``size()``, ``is_empty()``, ``comparator()``, ``ceiling_entry(key)``, ``ceiling_key(key)``, ``descending_key_set()``, ``descending_map()``, ``first_entry()``, ``floor_entry(key)``, ``floor_key(key)``, ``head_map(to_key, inclusive=False)``, ``higher_entry(key)``, ``higher_key(key)``, ``last_entry()``, ``lower_entry(key``, ``lower_key(key)``, ``navigable_key_set()``, ``poll_first_entry()``, ``poll_last_entry()``, ``sub_map(from_key, to_key, from_inclusive=True, to_inclusive=False)``, ``tail_map(from_key, inclusive=True)``, ``comparator()``, ``entry_set()``, ``first_key()``, ``last_key()``, ``key_set()``, ``values()``

Consult the :doc:`tree_map` section for more details.
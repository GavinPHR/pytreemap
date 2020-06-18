TreeMap
=======

.. class:: TreeMap(comparator=None)

   Constructor. You can supply a comparator if your keys
   do not implement rich comparison methods (you do not need this
   for most Python built-in objects). The comparator function
   should take 2 arguments ``a`` and ``b``,
   return a negative int if ``a < b``,
   return a positive int if ``a > b``,
   and return 0 if ``a == b``. E.g.
   ::

      def cmp(a, b):
          if a < b:
              return -1
          elif a > b:
              return 1
          else:
              return 0

   .. method:: size()

   Return the number of entries in the tree.
   You can also use the built-in ``len()`` function to get the size of the tree.

   .. method:: contains_key(key)

   Returns ``True`` if this map contains a mapping for the specified key.
   Returns ``False`` otherwise.

   .. method:: contains_value(value)

   Returns ``True`` if at least 1 key is mapped to the specified value.
   Returns ``False`` otherwise.

   .. method:: get(key)

   Returns the value to which the specified key is mapped to.
   Returns ``None`` is no such mapping exists.

   .. NOTE::
      You can also get the value using the ``self[key]`` syntax. Unlike
      :meth:`get`, a ``KeyError`` is raised if the key
      is not found.

   .. method:: comparator()

   Returns the comparator if you supplied one. Returns ``None`` otherwise.

   .. method:: first_key()

   Returns the first/smallest/left-most key.
   Returns ``None`` if no such key exists.

   .. method:: last_key()

   Returns the last/largest/right-most key.
   Returns ``None`` if no such key exists.

   .. method:: put(key, value)

   Associates the key with the value. If the key already exists,
   the old associated value is replaced with the new value.

   .. NOTE::
      You can also insert a key-value pair using the ``self[key] = value``
      syntax.

   .. method:: remove(key)

   If the key exists, remove the entry and return the associated value.
   Returns ``None`` otherwise.

   .. NOTE::
      You can also remove an entry using the ``del self[key]`` syntax.
      Unlike :meth:`put`, a ``KeyError`` is raised if the key is not found.

   .. method:: clear()

   Remove all entries and reset all the fields.

   .. method:: first_entry()

   Returns the first/smallest/left-most entry. The entry returned
   Returns ``None`` if no such entry exists.

   .. method:: last_entry()

   Returns the last/largest/right-most entry. The entry returned
   Returns ``None`` if no such entry exists.

   .. method:: poll_first_entry()

   Remove and return the first entry.
   Returns ``None`` if no such entry exists.

   .. method:: poll_last_entry

   Remove and return the last entry.
   Returns ``None`` if no such entry exists.

   .. method:: lower_entry(key)

   Returns the entry with the greatest key **less than** the specified key.
   Returns ``None`` if no such entry exists.

   .. method:: lower_key(key)

   Returns the greatest key **less than** the specified key.
   Returns ``None`` if no such key exists.

   .. method:: floor_entry(key)

   Returns the entry with the greatest key **less than or equal** to the specified key.
   Returns ``None`` if no such entry exists.

   .. method:: floor_key(key)

   Returns the greatest key **less than or equal** to the specified key.
   Returns ``None`` if no such key exists.

   .. method:: ceiling_entry(key)

   Returns the entry with the smallest key **greater than or equal to** the specified key.
   Returns ``None`` if no such entry exists.

   .. method:: ceiling_key(key)

   Returns the smallest key **greater than or equal to** the specified key.
   Returns ``None`` if no such key exists.

   .. method:: higher_entry(key)

   Returns the entry with the smallest key **greater than** the specified key.
   Returns ``None`` if no such entry exists.

   .. method:: higher_key(key)

   Returns the smallest key **greater than** the specified key.
   Returns ``None`` if no such key exists.

   .. method:: key_set()

   Returns a set view of all the keys in the map.
   The object returned is iterable and the iteration from the smallest to the largest key.

   .. method:: navigable_key_set()

   Same as :meth:`key_set`.

   .. method:: descending_key_set()

   Similar to :meth:`key_set` but the iteration goes from the largest to the smallest key.

   .. method:: values()

   Returns a collection view of the values in the map.
   The object returned is iterable.

   .. method:: entry_set()

   Returns a set view of the entries in the map.
   The object returned is iterable and the iteration
   from the entry with the smallest to the entry with the largest key.

   .. method:: descending_map()

   Similar to :meth:`entry_set` but the iteration goes
   from the entry with the largest key to the entry with the smallest key.

   .. method:: sub_map(from_key, to_key, from_inclusive=True, to_inclusive=False)

   Returns a view of the portion of this map whose keys range from from_key to to_key.
   The default includes from_key but excludes to_key.

   .. method:: head_map(to_key, inclusive=False)

   Returns a view of the portion of this map whose keys are less than (or equal to, if inclusive is true) to_key.

   .. method:: tail_map(self, from_key, inclusive=True)

   Returns a view of the portion of this map whose keys are greater than (or equal to, if inclusive is true) from_key.
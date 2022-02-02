TreeMap
=======

.. contents:: Contents
   :local:

Constructor Summary
-------------------

+---------------------------------------------+------------------------------------------------------+
| Constructor                                 | Description                                          |
+=============================================+======================================================+
| :class:`TreeMap(comparator=None) <TreeMap>` | | Constructs a new, empty TreeMap. You can supply a  |
|                                             | | comparator if your keys do not implement rich      |
|                                             | | comparison methods (you do not need this for most  |
|                                             | | Python built-in objects).                          |
+---------------------------------------------+------------------------------------------------------+

Methods Summary
---------------

+----------------------------------------------------------------------+----------------------------------------------------------+
| Method                                                               | Description                                              |
+======================================================================+==========================================================+
| :meth:`size() <TreeMap.size>`                                        | | Returns the number of entries in the tree.             |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`contains_key(key) <TreeMap.contains_key>`                     | | Returns ``True`` if this map contains a mapping        |
|                                                                      | | for the specified key. Returns ``False`` otherwise.    |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`contains_value(value) <TreeMap.contains_value>`               | | Returns ``True`` if at least 1 key is mapped to        |
|                                                                      | | the specified value. Returns ``False`` otherwise.      |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`get(key) <TreeMap.get>`                                       | | Returns the value to which the specified key is mapped |
|                                                                      | | to. Returns ``None`` is no such mapping exists.        |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`comparator() <TreeMap.comparator>`                            | | Returns the comparator if you supplied one.            |
|                                                                      | | Returns ``None`` otherwise.                            |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`first_key() <TreeMap.first_key>`                              | | Returns the first/smallest/left-most key.              |
|                                                                      | | ``KeyError`` is raised if no such key exists           |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`last_key() <TreeMap.last_key>`                                | | Returns the last/largest/right-most key.               |
|                                                                      | | ``KeyError`` is raised if no such key exists           |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`put(key, value) <TreeMap.put>`                                | | Associates the key with the value. If the key          |
|                                                                      | | already exists, the old associated value is            |
|                                                                      | | replaced with the new value.                           |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`remove(key) <TreeMap.remove>`                                 | | If the key exists, remove the entry and return the     |
|                                                                      | | associated value. Returns ``None`` otherwise.          |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`clear() <TreeMap.clear>`                                      | | Removes all entries and reset all the fields.          |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`first_entry() <TreeMap.first_entry>`                          | | Returns the first/smallest/left-most entry.            |
|                                                                      | | Returns ``None`` if no such entry exists.              |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`last_entry() <TreeMap.last_entry>`                            | | Returns the last/largest/right-most entry.             |
|                                                                      | | Returns ``None`` if no such entry exists.              |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`poll_first_entry() <TreeMap.poll_first_entry>`                | | Removes and returns the first entry.                   |
|                                                                      | | Returns ``None`` if no such entry exists.              |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`poll_last_entry() <TreeMap.poll_last_entry>`                  | | Removes and returns the last entry.                    |
|                                                                      | | Returns ``None`` if no such entry exists.              |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`lower_entry(key) <TreeMap.lower_entry>`                       | | Returns the entry with the greatest key                |
|                                                                      | | **less than** the specified key.                       |
|                                                                      | | Returns ``None`` if no such entry exists.              |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`lower_key(key) <TreeMap.lower_key>`                           | | Returns the greatest key **less than**                 |
|                                                                      | | the specified key.                                     |
|                                                                      | | Returns ``None`` if no such key exists.                |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`floor_entry(key) <TreeMap.floor_entry>`                       | | Returns the entry with the greatest key                |
|                                                                      | | **less than or equal** to the specified key.           |
|                                                                      | | Returns ``None`` if no such entry exists.              |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`floor_key(key) <TreeMap.floor_key>`                           | | Returns the greatest key **less than or equal**        |
|                                                                      | | to the specified key.                                  |
|                                                                      | | Returns ``None`` if no such key exists.                |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`ceiling_entry(key) <TreeMap.ceiling_entry>`                   | | Returns the entry with the smallest key                |
|                                                                      | | **greater than or equal to** the specified key.        |
|                                                                      | | Returns ``None`` if no such entry exists.              |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`ceiling_key(key) <TreeMap.ceiling_key>`                       | | Returns the smallest key                               |
|                                                                      | | **greater than or equal to** the specified key.        |
|                                                                      | | Returns ``None`` if no such key exists.                |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`higher_entry(key) <TreeMap.higher_entry>`                     | | Returns the entry with the smallest key                |
|                                                                      | | **greater than** the specified key.                    |
|                                                                      | | Returns ``None`` if no such entry exists.              |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`higher_key(key) <TreeMap.higher_key>`                         | | Returns the smallest key **greater than**              |
|                                                                      | | the specified key.                                     |
|                                                                      | | Returns ``None`` if no such key exists.                |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`key_set() <TreeMap.key_set>`                                  | | Returns a set view of all the keys in the map.         |
|                                                                      | | The object returned is iterable and the iteration      |
|                                                                      | | goes from the smallest to the largest key.             |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`navigable_key_set() <TreeMap.navigable_key_set>`              | | Same as :meth:`key_set() <TreeMap.key_set>`.           |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`descending_key_set() <TreeMap.descending_key_set>`            | | Similar to :meth:`key_set() <TreeMap.key_set>` but the |
|                                                                      | | iteration goes from the largest to the smallest key.   |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`values() <TreeMap.values>`                                    | | Returns a collection view of the values in the map.    |
|                                                                      | | The object returned is iterable.                       |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`entry_set() <TreeMap.entry_set>`                              | | Returns a set view of the entries in the map.          |
|                                                                      | | The object returned is iterable and the iteration      |
|                                                                      | | from the entry with the smallest to the entry with     |
|                                                                      | | the largest key.                                       |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`descending_map() <TreeMap.descending_map>`                    | | Returns a reverse order view of the map.               |
+----------------------------------------------------------------------+----------------------------------------------------------+
| | :meth:`sub_map(from_key, to_key, <TreeMap.sub_map>`                | | Returns a view of the portion of this map whose        |
| | :meth:`from_inclusive=True, to_inclusive=False) <TreeMap.sub_map>` | | keys range from from_key to to_key.                    |
|                                                                      | | The default includes from_key but excludes to_key.     |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`head_map(to_key, inclusive=False) <TreeMap.head_map>`         | | Returns a view of the portion of this map whose        |
|                                                                      | | keys are less than (or equal to, if inclusive is       |
|                                                                      | | true) to_key.                                          |
+----------------------------------------------------------------------+----------------------------------------------------------+
| :meth:`tail_map(from_key, inclusive=True) <TreeMap.tail_map>`        | | Returns a view of the portion of this map whose        |
|                                                                      | | keys are greater than (or equal to, if inclusive       |
|                                                                      | | is true) from_key.                                     |
+----------------------------------------------------------------------+----------------------------------------------------------+

Methods ``is_empty()``, ``put_all()``, ``equals()``, ``hash_code()``,
``to_string()``, ``get_or_default()``, ``for_each()``, ``replace_all()``,
``put_if_absent()``, ``replace()``, ``compute_if_absent()``,
``compute_if_present()``, ``compute()`` and classes ``SimpleEntry``,
``SimpleImmutableEntry``, ``Entry`` are also implemented. For advanced users,
please consult the source code.

Constructor and Methods Details
-------------------------------



.. class:: TreeMap(comparator=None)

   Constructs a new, empty TreeMap. You can supply a comparator if your keys
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

      Returns the number of entries in the tree.

      .. TIP::
         You can also use the built-in ``len()`` function to get the size of the tree.

   .. method:: contains_key(key)

      Returns ``True`` if this map contains a mapping for the specified key.
      Returns ``False`` otherwise.

      :raises TypeError: If ``key`` is not comparable to the keys currently in the map.

      .. TIP::
         You can also use the ``key in self`` syntax to check whether
         the map contains the ky.

   .. method:: contains_value(value)

      Returns``True`` if at least 1 key is mapped to the specified value.
      Returns ``False`` otherwise.

   .. method:: get(key)

      Returns the value to which the specified key is mapped to.
      Returns ``None`` is no such mapping exists.

      :raises TypeError: If ``key`` is not comparable to the keys currently in the map.

      .. TIP::
         You can also get the value using the ``self[key]`` syntax. Unlike
         :meth:`get`, a ``KeyError`` is raised if the key
         is not found.

   .. method:: comparator()

      Returns the comparator if you supplied one. Returns ``None`` otherwise.

   .. method:: first_key()

      Returns the first/smallest/left-most key.

      :raise KeyError: if the map is empty

   .. method:: last_key()

      Returns the last/largest/right-most key.

      :raise KeyError: if the map is empty

   .. method:: put(key, value)

      Associates the key with the value. If the key already exists,
      the old associated value is replaced with the new value.

      :raises TypeError: If ``key`` is not comparable to the keys currently in the map.

      .. TIP::
         You can also insert a key-value pair using the ``self[key] = value``
         syntax.

   .. method:: remove(key)

      If the key exists, remove the entry and return the associated value.
      Returns ``None`` otherwise.

      :raises TypeError: If ``key`` is not comparable to the keys currently in the map.

      .. TIP::
         You can also remove an entry using the ``del self[key]`` syntax.
         Unlike :meth:`put`, a ``KeyError`` is raised if the key is not found.

   .. method:: clear()

      Removes all entries and reset all the fields.

   .. method:: first_entry()

      Returns the first/smallest/left-most entry.
      Returns ``None`` if no such entry exists.

      :rtype: :doc:`entry`

   .. method:: last_entry()

      Returns the last/largest/right-most entry.
      Returns ``None`` if no such entry exists.

      :rtype: :doc:`entry`

   .. method:: poll_first_entry()

      Removes and returns the first entry.
      Returns ``None`` if no such entry exists.

      :rtype: :doc:`entry`

   .. method:: poll_last_entry()

      Removes and returns the last entry.
      Returns ``None`` if no such entry exists.

      :rtype: :doc:`entry`

   .. method:: lower_entry(key)

      Returns the entry with the greatest key **less than** the specified key.
      Returns ``None`` if no such entry exists.

      :rtype: :doc:`entry`
      :raises TypeError: If ``key`` is not comparable to the keys currently in the map.

   .. method:: lower_key(key)

      Returns the greatest key **less than** the specified key.
      Returns ``None`` if no such key exists.

      :raises TypeError: If ``key`` is not comparable to the keys currently in the map.

   .. method:: floor_entry(key)

      Returns the entry with the greatest key **less than or equal** to the specified key.
      Returns ``None`` if no such entry exists.

      :rtype: :doc:`entry`
      :raises TypeError: If ``key`` is not comparable to the keys currently in the map.

   .. method:: floor_key(key)

      Returns the greatest key **less than or equal** to the specified key.
      Returns ``None`` if no such key exists.

      :raises TypeError: If ``key`` is not comparable to the keys currently in the map.

   .. method:: ceiling_entry(key)

      Returns the entry with the smallest key **greater than or equal to** the specified key.
      Returns ``None`` if no such entry exists.

      :rtype: :doc:`entry`
      :raises TypeError: If ``key`` is not comparable to the keys currently in the map.

   .. method:: ceiling_key(key)

      Returns the smallest key **greater than or equal to** the specified key.
      Returns ``None`` if no such key exists.

      :raises TypeError: If ``key`` is not comparable to the keys currently in the map.

   .. method:: higher_entry(key)

      Returns the entry with the smallest key **greater than** the specified key.
      Returns ``None`` if no such entry exists.

      :rtype: :doc:`entry`
      :raises TypeError: If ``key`` is not comparable to the keys currently in the map.

   .. method:: higher_key(key)

      Returns the smallest key **greater than** the specified key.
      Returns ``None`` if no such key exists.

      :raises TypeError: If ``key`` is not comparable to the keys currently in the map.

   .. method:: key_set()

      Returns a set view of all the keys in the map.
      The object returned is iterable and the iteration goes from the smallest to the largest key.

      :rtype: :doc:`navigable_set`

   .. method:: navigable_key_set()

      Same as :meth:`key_set`.

      :rtype: :doc:`navigable_set`

   .. method:: descending_key_set()

      Similar to :meth:`key_set` but the iteration goes from the largest to the smallest key.

      :rtype: :doc:`navigable_set`

   .. method:: values()

      Returns a collection view of the values in the map.
      The object returned is iterable.

      :rtype: :doc:`values`

   .. method:: entry_set()

      Returns a set view of the entries in the map.
      The object returned is iterable and the iteration
      from the entry with the smallest to the entry with the largest key.

      :rtype: :doc:`entry_set`

   .. method:: descending_map()

      Returns a reverse order view of the map.

     :rtype: :doc:`navigable_map`

   .. method:: sub_map(from_key, to_key, from_inclusive=True, to_inclusive=False)

      Returns a view of the portion of this map whose keys range from from_key to to_key.
      The default includes from_key but excludes to_key.

      :rtype: :doc:`navigable_map`
      :raises TypeError: If ``from_key`` or ``to_key`` is not comparable to the keys currently in the map.
      :raises KeyError: If ``from_key`` is greater than ``to_key``;
                        or if this map itself has a restricted range,
                        and ``from_key`` or ``to_key`` lies outside the bounds of the range.

   .. method:: head_map(to_key, inclusive=False)

      Returns a view of the portion of this map whose keys are less than (or equal to, if inclusive is true) to_key.

      :raises TypeError: If ``to_key`` is not comparable to the keys currently in the map.
      :raises KeyError: If this map itself has a restricted range,
                        and ``to_key`` lies outside the bounds of the range.

   .. method:: tail_map(from_key, inclusive=True)

      Returns a view of the portion of this map whose keys are greater than (or equal to, if inclusive is true) from_key.

      :raises TypeError: If ``from_key`` is not comparable to the keys currently in the map.
      :raises KeyError: If this map itself has a restricted range,
                        and ``from_key`` lies outside the bounds of the range.
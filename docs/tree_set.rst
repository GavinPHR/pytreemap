TreeSet
=======

.. NOTE::
   :doc:`tree_set` is essentially :doc:`tree_map` with dummy values.
   So only constructor and methods summaries are provided here.

.. contents:: Contents
   :local:

Constructor Summary
-------------------

+------------------------------+-----------------------------------------------------+
| Constructor                  | Description                                         |
+==============================+=====================================================+
| ``TreeSet(comparator=None)`` | | Constructs a new, empty TreeSap. You can supply a |
|                              | | comparator if your elements do not implement rich |
|                              | | comparison methods (you do not need this for most |
|                              | | Python built-in objects).                         |
+------------------------------+-----------------------------------------------------+

Methods Summary
---------------

+------------------------------------------------+-------------------------------------------------------+
| Method                                         | Description                                           |
+================================================+=======================================================+
| ``iterator()``                                 | | Returns an iterator that iterates the elements      |
|                                                | | from the smallest to the largest.                   |
+------------------------------------------------+-------------------------------------------------------+
| ``descending_iterator()``                      | | Similar to ``iterator()`` but the iteration         |
|                                                | | goes from the largest element to the smallest.      |
+------------------------------------------------+-------------------------------------------------------+
| ``descending_set()``                           | | Returns a reverse order view of the elements.       |
+------------------------------------------------+-------------------------------------------------------+
| ``size()``                                     | | Returns the number of elements in the set.          |
+------------------------------------------------+-------------------------------------------------------+
| ``is_empty()``                                 | | Returns ``True`` if the set contains no element.    |
+------------------------------------------------+-------------------------------------------------------+
| ``contains(o)``                                | | Returns ``True`` if this map contains the           |
|                                                | | specified element. Returns ``False`` otherwise.     |
+------------------------------------------------+-------------------------------------------------------+
| ``add(e)``                                     | | Adds the specified element to the set if            |
|                                                | | it is not already present.                          |
+------------------------------------------------+-------------------------------------------------------+
| ``remove(o)``                                  | | Removes the specified element if present            |
+------------------------------------------------+-------------------------------------------------------+
| ``clear()``                                    | | Removes all elements.                               |
+------------------------------------------------+-------------------------------------------------------+
| | ``sub_map(from_element, to_element``         | | Returns a view of the portion of this set whose     |
| | ``from_inclusive=True, to_inclusive=False)`` | | elements range from from_element to to_element.     |
|                                                | | The default includes from_element but               |
|                                                | | excludes to_element.                                |
+------------------------------------------------+-------------------------------------------------------+
| ``head_map(to_element, inclusive=False)``      | | Returns a view of the portion of this set whose     |
|                                                | | elements are less than (or equal to, if             |
|                                                | | inclusive is true) to_elemnt.                       |
+------------------------------------------------+-------------------------------------------------------+
| ``tail_map(from_element, inclusive=True)``     | | Returns a view of the portion of this set whose     |
|                                                | | elements are greater than (or equal to, if          |
|                                                | | inclusive is true) from_element.                    |
+------------------------------------------------+-------------------------------------------------------+
| ``comparator()``                               | | Returns the comparator if you supplied one.         |
|                                                | | Returns ``None`` otherwise.                         |
+------------------------------------------------+-------------------------------------------------------+
| ``first()``                                    | | Returns the first/smallest/left-most element.       |
|                                                | | ``KeyError`` is raised if no such element exists.   |
+------------------------------------------------+-------------------------------------------------------+
| ``last()``                                     | | Returns the last/largest/right-most element.        |
|                                                | | ``KeyError`` is raised if no such element exists    |
+------------------------------------------------+-------------------------------------------------------+
| ``lower(e)``                                   | | Returns the greatest element **less than**          |
|                                                | | the specified element.                              |
|                                                | | Returns ``None`` if no such element exists.         |
+------------------------------------------------+-------------------------------------------------------+
| ``floor(e)``                                   | | Returns the greatest element                        |
|                                                | | **less than or equal** to the specified element.    |
|                                                | | Returns ``None`` if no such element exists.         |
+------------------------------------------------+-------------------------------------------------------+
| ``ceiling(e)``                                 | | Returns the smallest element                        |
|                                                | | **greater than or equal to** the specified element. |
|                                                | | Returns ``None`` if no such element exists.         |
+------------------------------------------------+-------------------------------------------------------+
| ``higher(e)``                                  | | Returns the smallest element **greater than**       |
|                                                | | the specified element.                              |
|                                                | | Returns ``None`` if no such element exists.         |
+------------------------------------------------+-------------------------------------------------------+
| ``poll_first()``                               | | Removes and returns the first element.              |
|                                                | | Returns ``None`` if no such element exists.         |
+------------------------------------------------+-------------------------------------------------------+
| ``poll_last()``                                | | Removes and returns the last element.               |
|                                                | | Returns ``None`` if no such element exists.         |
+------------------------------------------------+-------------------------------------------------------+

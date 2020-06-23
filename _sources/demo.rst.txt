Usage Demo
==========

This demo aims to show you the basic operations available in this package.

Import and instantiate
----------------------

.. code-block::

   >>> from pytreemap import TreeMap
   >>> tm = TreeMap()

Insert key-value mappings
-------------------------

.. code-block::

   >>> tm[5] = 'Python is great!'
   >>> print(tm)
   {5=Python is great!}
   >>> tm[10] = 'Java is also nice!'
   >>> print(tm)
   {5=Python is great!, 10=Java is also nice!}
   >>> tm.put(-1,  'We love them both!')
   >>> print(tm)
   {-1=We love them both!, 5=Python is great!, 10=Java is also nice!}

Search for keys
---------------

.. code-block::

   >>> tm[5]
   'Python is great!'
   >>> tm[2]
   KeyError: 'key not found'
   >>> tm.get(2)  # No error is raised

Delete key-value mappings
-------------------------

.. code-block::

   >>> del tm[10]
   >>> print(tm)
   {-1=We love them both!, 5=Python is great!}
   >>> del tm[2]
   KeyError: 'key not found'
   >>> tm.remove(2)  # No error is raised

Check whether some keys exist
-----------------------------

.. code-block::

   >>> 2 in tm
   False
   >>> -1 in tm
   True
   >>> tm.contains_key(-1)
   True

Iterate over keys/values/entries
--------------------------------

.. code-block::

   >>> [key for key in tm]
   [-1, 5]
   >>> [key for key in tm.key_set()]
   [-1, 5]
   >>> [value for value in tm.values()]
   ['We love them both!', 'Python is great!']
   >>> [entry for entry in tm.entry_set()]
   [-1=We love them both!, 5=Python is great!]


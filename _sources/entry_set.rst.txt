EntrySet
========

EntrySet objects returned by TreeMap's methods are views on the calling TreeMap instance. EntrySet supports these methods:

``remove(o)`` removes the entry o from the underlying TreeMap instance.

``clear()`` clears the underlying TreeMap instance.

``to_list()`` returns a Python list of all the entries in the underlying TreeMap.

EntrySet instances can be checked for equality (``==``), represented using strings (``print()`` or ``str()``), hashed (``hash()``), iterated (``iter()``), and checked for membership (``element in self``).


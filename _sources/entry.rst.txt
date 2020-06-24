Entry
=====

Entry supports 3 methods:

``get_key()`` returns the key of the entry.

``get_value()`` returns the value of the entry.

``set_value(value)`` replaces the current value with the specified value and returns the replaced value.

.. DANGER::
   Entry objects returned by TreeMap's methods designed to be immutable.

Entry can be checked for equality (``==``), represented using strings (``print()`` or ``str()``), and hashed (``hash()``).

.. TIP::
   For more advanced users, you can accessed the key, value, left child, right child, parent, and color of an entry using 
   ``self.key``, ``self.value``, ``self.left``,
   ``self.right``, ``self.parent``, and ``self.color``, respectively.


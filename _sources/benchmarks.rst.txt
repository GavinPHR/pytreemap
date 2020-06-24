Benchmarks
==========

All benchmarks are done on a laptop with 
Intel Core i7-7700HQ CPU and 16GB of RAM.

Since this package is an implementation
of the Java TreeMap, the benchmarks 
are focused on comparing the performance 
between this package and Java's TreeMap. 

This package is currently written in pure
Python and it should come at no surprise
that it is much slower than Java, especially
when the size of the tree is large.

.. NOTE::
   A Cython version is in the works.

Benchmark procedure:

1. Prepare :math:`n` entries with distinct keys. (:math:`n` ranges from 1000 to 60000 with 1000 interval.)
2. Insert/Remove/Search them into the map in random order and record the completion time.
3. Repeat step 1-2 two more times and average the result.

Here is result using Java TreeMap:

.. image:: ../benchmarks/java.png
   :width: 500px
   :align: center

And here is the result using pytreemap:

.. image:: ../benchmarks/pytreemap.png
   :width: 500px
   :align: center

Overlay the plots together, we can see that pytreemap is ~30x slower:

.. image:: ../benchmarks/java_vs_pytreemap.png
   :width: 500px
   :align: center


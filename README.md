# pytreemap [![Build Status](https://travis-ci.com/GavinPHR/pytreemap.svg?branch=master)](https://travis-ci.com/GavinPHR/pytreemap) [![codecov](https://codecov.io/gh/GavinPHR/pytreemap/branch/master/graph/badge.svg)](https://codecov.io/gh/GavinPHR/pytreemap) ![](https://img.shields.io/pypi/v/pytreemap) ![](https://img.shields.io/badge/python-%3E%3D3.5-blue) ![](https://img.shields.io/github/license/GavinPHR/pytreemap)
Python implementation of the Java TreeMap/Tree.

 - [Installation](#installation)
 - [Documentation](#documentation)
 - [Basic Usage](#basic-usage)
 - [Testings](#testing)
 - [Benchmarks](#benchmarks)

## Installation

Install with pip:

```bash
pip install pytreemap
```

## Documentation
[Click here to access the documentation](https://gavinphr.github.io/pytreemap/)

## Basic Usage

This demo aims to show you the basic operations available in this package.
Consult the [documentation]((https://gavinphr.github.io/pytreemap/)) for more details.

### Import and instantiate

```python
>>> from pytreemap import TreeMap
>>> tm = TreeMap()
```
   
### Insert key-value mappings

```python
>>> tm[5] = 'Python is great!'
>>> print(tm)
{5=Python is great!}
>>> tm[10] = 'Java is also nice!'
>>> print(tm)
{5=Python is great!, 10=Java is also nice!}
>>> tm.put(-1,  'We love them both!')
>>> print(tm)
{-1=We love them both!, 5=Python is great!, 10=Java is also nice!}
```

### Search for keys

```python
>>> tm[5]
'Python is great!'
>>> tm[2]
KeyError: 'key not found'
>>> tm.get(2)  # No error is raised
```

### Delete key-value mappings

```python
>>> del tm[10]
>>> print(tm)
{-1=We love them both!, 5=Python is great!}
>>> del tm[2]
KeyError: 'key not found'
>>> tm.remove(2)  # No error is raised
```

### Check whether some keys exist

```python
>>> 2 in tm
False
>>> -1 in tm
True
>>> tm.contains_key(-1)
True
```

### Iterate over keys/values/entries

```python
>>> [key for key in tm]
[-1, 5]
>>> [key for key in tm.key_set()]
[-1, 5]
>>> [value for value in tm.values()]
['We love them both!', 'Python is great!']
>>> [entry for entry in tm.entry_set()]
[-1=We love them both!, 5=Python is great!]
```

## Testing 
Most of the tests from Java that concerned TreeMap are passed. Check out the tests/ directory for more details.

## Benchmarks
All benchmarks are done on a laptop with Intel Core i7-7700HQ CPU and 16GB of RAM.

Since this package is an implementation of the Java TreeMap, the benchmarks are focused on comparing the performance between this package and Java’s TreeMap.

This package is currently written in pure Python and it should come at no surprise that it is much slower than Java, especially when the size of the tree is large.

A Cython version is in the works.

Benchmark procedure:

1. Prepare n entries with distinct keys. (n ranges from 1000 to 60000 with 1000 interval.)

2. Insert/Remove/Search them into the map in random order and record the completion time.

3. Repeat step 1-2 two more times and average the result.

Here is result using Java TreeMap:

<p align="center">
<img src="https://raw.githubusercontent.com/GavinPHR/pytreemap/master/benchmarks/java.png" width="450"/>
</p>

And here is the result using pytreemap:

<p align="center">
<img src="https://raw.githubusercontent.com/GavinPHR/pytreemap/master/benchmarks/pytreemap.png" width="450"/>
</p>

Overlay the plots together, we can see that pytreemap is ~30x slower:

<p align="center">
<img src="https://raw.githubusercontent.com/GavinPHR/pytreemap/master/benchmarks/java_vs_pytreemap.png" width="450"/>
</p>


import sys
from time import time_ns
from pytreemap import TreeMap
from random import shuffle

def time(store):
    tm = TreeMap()
    for i in store:
        tm.put(i, i)
    start = time_ns()
    for i in store:
        tm.get(i)
    end = time_ns()
    return end - start

if __name__ == '__main__':
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
        trial = 5
    elif len(sys.argv) == 3:
        n = int(sys.argv[1])
        trial = int(sys.argv[2])
    else:
        raise RuntimeError('must have 1 or 2 args')

    store = [0]*n
    for i in range(n):
        store[i] = n-i-1

    result = 0
    for _ in range(trial):
        shuffle(store)
        result += time(store)
    result //= trial
    print(result/1000000)

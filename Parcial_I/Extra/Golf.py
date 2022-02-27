import math
import functools
import sys
sys.setrecursionlimit(15000)

def memoize(func):
    cache = {}
 
    def memoized(key):
        # Returned, new, memoized version of decorated function
        if key not in cache:
            cache[key] = func(key)
        return cache[key]
    return functools.update_wrapper(memoized, func)

def main():
    for i in range(0, 20):
        cn = c(i)
        trib1 = trib(cn + 1)
        ctrib = c(trib1)
        log = math.log(ctrib,2)
        floor = math.floor(log)
        print("{}, {}, {}, {}, {}".format(cn, trib1, ctrib, log, floor))


def c(n):
    return 1 if n == 0 else (
        ((4 * n - 2) * c(n - 1)) // (n + 1)
    )

def trib(n):
    if n < 3:
        return n
    return trib(n-1) + trib(n-2) + trib(n-3)

if __name__ == '__main__':
    main()
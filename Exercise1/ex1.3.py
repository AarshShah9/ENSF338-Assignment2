def func(n, cache):
    if n == 0 or n == 1:
        return n
    elif n in cache:
        return cache[n]
    else:
        cache[n] = func(n-1, cache) + func(n-2, cache)
        return cache[n]
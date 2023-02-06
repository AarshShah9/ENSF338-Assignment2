def func(n, cache):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        cache[n] = func(n-1, cache) + func(n-2, cache)
        return cache[n]
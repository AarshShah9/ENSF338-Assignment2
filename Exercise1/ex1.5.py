import timeit
import matplotlib.pyplot as plt


def nomemo(n):
    if n == 0 or n == 1:
        return n
    else:
        return nomemo(n-1) + nomemo(n-2)


def memo(n, cache):
    if n == 0 or n == 1:
        return n
    elif n in cache:
        return cache[n]
    else:
        cache[n] = memo(n-1, cache) + memo(n-2, cache)
        return cache[n]


original_times = []
memo_times = []

for n in range(0, 36):
    original_times.append(timeit.timeit(lambda: nomemo(n), number=100))
    memo_times.append(timeit.timeit(lambda: memo(n, cache={}), number=100))

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(range(0, 36), original_times,
            label='Original', marker='.', c="blue")
ax1.scatter(range(0, 36), memo_times, label='Memoized', c="red", marker='.')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.legend(loc='upper left')
plt.show()

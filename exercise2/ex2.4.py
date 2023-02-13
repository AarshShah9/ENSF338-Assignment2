import random
import timeit
import matplotlib.pyplot as plt
import urllib.request
import json


def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)


def func2(array, start, end):
    # Select a random pivot
    pivot_index = random.randint(start, end)
    array[start], array[pivot_index] = array[pivot_index], array[start]

    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


def timing():

    times = []
    lengths = []

    with urllib.request.urlopen('https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment2/ex2.json') as inUrl:
        content = json.load(inUrl)

        for i, array in enumerate(content):
            lengths.append(len(array))
            times.append(timeit.timeit(lambda: func1(
                array, 0, len(array)-1), number=5))
            print(f"Time for array {i + 1} in seconds", times[i]/1000.0)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    ax1.scatter(lengths, times, label='Original', marker='.', c="blue")

    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.legend(loc='upper left')
    plt.show()


def main():
    timing()


if __name__ == "__main__":
    main()

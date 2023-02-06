import urllib.request
import sys
import json
import timeit
import math
sys.setrecursionlimit(20000)


def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)


def func2(array, start, end):
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

    with urllib.request.urlopen('https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment2/ex2.json') as inUrl:
        content = json.load(inUrl)

        for i, array in enumerate(content):
            rez = timeit.timeit(lambda: func1(
                array, 0, len(array)-1), number=10)
            print(f"Time for array {i + 1} in seconds", rez/1000.0)
            # val = len(array) * math.log(len(array), 2)
            # print(f"Calculating {len(array)}(log({len(array)}) = {val}")


def main():
    timing()


if __name__ == "__main__":
    main()

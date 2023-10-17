from collections import Counter
import timeit

def func1(text):
    d = {}
    for word in text.split():
        if d.get(word):
            d[word] += 1
        else:
            d[word] = 1
    return d

def func2(text):
    return Counter(text.split())

text = input()
print(timeit.timeit('func1(text)', globals=globals()))
print(timeit.timeit('func2(text)', globals=globals()))

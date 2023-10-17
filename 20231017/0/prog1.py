import timeit

print(timeit.Timer(input(), setup='import timeit').autorange())

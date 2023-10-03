def func(a, b):
    return lambda x: a * x + b

f = func(2, 1)
print(f(int(input())))

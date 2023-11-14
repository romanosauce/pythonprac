def type_check(fun):
    def wrapper(*args):
        if any(type(i) != int for i in args):
            raise TypeError
        return fun(*args)
    return wrapper

@type_check
def f(a, b, c):
    return 1

print(f(1, 2, 3))
print(f('a', 1, 2))

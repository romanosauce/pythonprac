from functools import wraps

from functools import wraps
def debug(fun):
    @wraps(fun)
    def wrapper(*args):
        print('<', *args)
        res = fun(*args)
        print('>', res)
        return res
    return wrapper
@debug
def mult(a, b):
    "asdlfkj"
    return a * b
print(mult, mult.__doc__)

import inspect


def output_name_and_param(fun):
    def new_fun(*args, **kwargs):
        print(f"{fun.__name__}: {args[1:]}, {kwargs}")
        res = fun(*args, **kwargs)
        return res
    return new_fun


class dump(type):
    def __init__(cls, name, bases, ns):
        for method in cls.__dict__:
            obj = getattr(cls, method)
            if inspect.isfunction(obj):
                setattr(cls, method, output_name_and_param(obj))
        return super().__init__(name, bases, ns)

import sys
exec(sys.stdin.read())

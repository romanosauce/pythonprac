lowercase = 'abcdefghijklmnopqrstuvwxyz'


class Alpha:
    __slots__ = [i for i in lowercase]

    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self, **kwargs):
        res = ''
        for elem in self.__slots__:
            value = getattr(self, elem, None)
            if value is not None:
                res += f"{elem}: {value}, "
        if res:
            return res[:-2]
        else:
            return res


class AlphaQ:
    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __setattr__(self, name, value):
        if name not in lowercase or len(name) != 1:
            raise AttributeError
        self.__dict__[name] = value

    def __getattr__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]
        else:
            raise AttributeError

    def __str__(self):
        res = ''
        for elem in lowercase:
            value = getattr(self, elem, None)
            if value is not None:
                res += f"{elem}: {value}, "
        if res:
            return res[:-2]
        else:
            return res


import sys
exec(sys.stdin.read())

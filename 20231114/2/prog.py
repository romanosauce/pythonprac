class Num:
    def __set_name__(self, obj, name):
        self.public_name = name
        self.private_name = '_' + name

    def __set__(self, obj, value):
        if 'real' in dir(value):
            setattr(obj, self.private_name, value)
            return
        if '__len__' in dir(value):
            setattr(obj, self.private_name, len(value))

    def __get__(self, obj, cls):
        try:
            return getattr(obj, self.private_name)
        except AttributeError:
            return 0


import sys
exec(sys.stdin.read())

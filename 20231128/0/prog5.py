from inspect import get_annotations


class C:
    a: int

    def __init__(self, a):
        print(get_annotations(self.__class__))

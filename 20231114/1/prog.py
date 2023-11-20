def objcount(cls):
    class NewClass(cls):
        counter = 0

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.__class__.counter += 1

        def __del__(self):
            try:
                super().__del__()
            except AttributeError:
                pass
            self.__class__.counter -= 1

    return NewClass


import sys
exec(sys.stdin.read())

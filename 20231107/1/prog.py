import collections


class DivStr(collections.UserString):
    def __init__(self, data=''):
        super().__init__(data)

    def __floordiv__(self, n):
        sub_len = len(self.data) // n
        for i in range(n):
            yield DivStr(self.data[i*sub_len:(i+1)*sub_len])

    def __mod__(self, n):
        sub_len = len(self.data) // n
        return DivStr(self.data[sub_len * n:])


import sys
exec(sys.stdin.read())

class Rectangle:
    rectcnt = 0

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.__class__.rectcnt += 1
        setattr(self, f"rect_{self.rectcnt}", self.rectcnt)

    def __str__(self):
        return f"({self.x1},{self.y1})({self.x1},{self.y2})\
({self.x2},{self.y2})({self.x2},{self.y1})  {self.__class__.rectcnt}"

    def __lt__(self, obj):
        return abs(self) < abs(obj)

    def __eq__(self, obj):
        return abs(self) == abs(obj)

    def __abs__(self):
        return abs((self.x1 - self.x2) * (self.y1 - self.y2))

    def __mul__(self, obj):
        return self.__class__(self.x1*obj, self.y1*obj,
                              self.x2*obj, self.y2*obj)

    def __rmul__(self, obj):
        return self.__class__(self.x1*obj, self.y1*obj,
                              self.x2*obj, self.y2*obj)

    def __getitem__(self, i):
        return ((self.x1, self.y1), (self.x1, self.y2),
                (self.x2, self.y2), (self.x2, self.y1))[i]

    def __bool__(self):
        return abs(self) != 0

    def __del__(self):
        self.__class__.rectcnt -= 1
        print('KILL KILL KILL KILL KILL ULTRAKIIIIIILLLLL')

# 102876 298762 19234 666234 1234
# 6987234 1346 8631 862346
# 631 632 test. Please 923 done 715 k1 ke_46
# 8356 function 8826__1nit__92734 obligate 99 LLL
# 34634923465 3354762391

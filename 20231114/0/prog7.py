class C:
    @property
    def age(self):
        if self.val == 42:
            print('secret value!')
            return -1
        else:
            return self.val

    @age.setter
    def age(self, value):
        if value > 128:
            raise ValueError("too old!")
        self.val = value


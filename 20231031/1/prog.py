class Omnibus:
    global_attr_dict = {}

    def __init__(self):
        self.local_attr_set = set()

    def __setattr__(self, name, value):
        if name == 'local_attr_set':
            self.__dict__['local_attr_set'] = set()
        elif name not in self.local_attr_set:
            self.local_attr_set.add(name)
            if name in self.global_attr_dict:
                self.global_attr_dict[name] += 1
            else:
                self.global_attr_dict[name] = 1

    def __getattribute__(self, name):
        if name == 'global_attr_dict' or (name == 'local_attr_set' or
                                          name == '__dict__'):
            return object.__getattribute__(self, name)
        return object.__getattribute__(self, 'global_attr_dict')[name]

    def __delattr__(self, name):
        if name in self.local_attr_set:
            self.local_attr_set.remove(name)
            self.global_attr_dict[name] -= 1

import sys
exec(sys.stdin.read())

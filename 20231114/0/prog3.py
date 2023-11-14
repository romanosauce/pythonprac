def type_check(inst):
    def type_checker(fun):
        def wrapper(*args, **kwargs):
            if all(isinstance(i, inst) for i in args) and \
               all(isinstance(j, inst) for j in kwargs):
                return fun(*args, **kwargs)
            else:
                raise TypeError
        return wrapper
    return type_checker

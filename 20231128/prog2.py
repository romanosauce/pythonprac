class Doubleton(type):
    _instance = []
    _obj_counter = 0
    def __call__(cls, *args, **kwargs):
        if cls._obj_counter == 2:
            return cls._instance[1]
        else:
            cls._obj_counter += 1
            obj = super().__call__(*args, **kwargs)
            cls._instance.append(obj)
            return obj

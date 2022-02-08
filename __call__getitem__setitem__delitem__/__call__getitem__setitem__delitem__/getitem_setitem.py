
#метод __getitem__, __setitem__, __delitem__

class Vector:
    
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)
    
    def __getitem__(self, item):
        if 1<=item<=len(self.values):
            return self.values[item-1]#изменяем порядок с 0 на 1
        else:
            raise IndentationError("ИНДЕКС ЗА ГРАНИЦАМИ НАЩЕЙ КОЛЛЕКЦИИ")

    def __setitem__(self, key, value):
        if 1<=key<=len(self.values):
            self.values[key-1] = value
        elif key>len(self.values):
            diff = key-len(self.values)
            self.values.extend([0]*diff)
            self.values[key-1] = value

        else:
            raise IndentationError("ИНДЕКС ЗА ГРАНИЦАМИ НАЩЕЙ КОЛЛЕКЦИИ")

    def __delitem__(self, key):
        if 0<= key <len(self.values):
            del self.values[key]
        else:
            raise IndentationError("ИНДЕКС ЗА ГРАНИЦАМИ НАЩЕЙ КОЛЛЕКЦИИ")


v1 = Vector(1,23,332,212)
v2 = Vector(212,2131,2121)
v3= Vector(121,3123,12,121,1)
v5=Vector(21,2131,31,21,2)
v6=Vector(213,121,2,1)
v7=Vector(423,2,42,32,2)
v8 = Vector(213,1,22)
v8[10]=100
print(v8)
print(v7[4])
del v6[2]
print(v6)
v5[2]=100
print(v5)
print(v3[3])
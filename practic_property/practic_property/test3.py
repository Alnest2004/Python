
class A:

    def __init__(self):
        self.__x = 12
        self.__y = 42

    @property
    def var(self):
        return f'X: {self.__x}, Y: {self.__y}'

    @var.setter
    def var(self, val, val2=None):
        if val2 is not None:
            self.__y = val2

        self.__x = val

    #var = property(get_var, set_var)



a = A()
print(a.var)  # X: 12, Y: 42
a.var = 678
print(a.var) # X: 678, Y: 42
a.var(3, 77)
print(a.var)  # X: 3, Y: 77

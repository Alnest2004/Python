class NoDataDescr:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return "NoDataDescr __get__"


class CoordValue:
    def __set_name__(self, owner, name):
        print(name)
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name]=value



class Point:
    noData= NoDataDescr()

    coordX=CoordValue()
    coordY = CoordValue()
    def __init__(self, x=0, y=0):
        self.coordX=x
        self.coordY=y



pt = Point(1,2)
pt2 = Point(10,20)
print(pt.coordX, pt.coordY)
print(pt2.coordX, pt2.coordY)



class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        print('get balance')
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    #my_balance = my_property_balance.setter(my_balance)#почти тоже самое что и @my_balance.setter
    
#
    #@my_balance.deleter
    #def my_balance(self):
    #    print('delete balance')
    #    del self.__balance
#
    #my_balance = property(my_balance)#происходит тоже самое что и @property
    #my_balance= my_balance.setter(set_balance)
    #my_balance= my_balance.deleter(delete_balance)

p=BankAccount('TOD', 999)
p.my_balance = 901
print(p.my_balance)

#del p.my_balance




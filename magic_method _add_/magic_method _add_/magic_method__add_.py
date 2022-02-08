
"""
__len__() – позволяет применять функцию len() к экземплярам класса;
__abs__() - позволяет применять функцию abs() к экземплярам класса.
"""



class Point:
    def __init__(self, *args):
        self.__coords = args
    # здесь возвращаем размер списка __coords
    def __len__(self):
        return len(self.__coords)
    def __abs__(self):
        return list( map(abs, self.__coords) )
p = Point(1, 2, -3)
print(abs(p))
print( len(p) )

class BankAccount:
    def __init__(self, name, balance):
        print('new_object init')
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f"Клиент {self.name} с балансом {self.balance}"

    
    def __add__(self, other):
        print('метод __add__')
        if isinstance(other, BankAccount):
            return self.balance +other.balance
        if isinstance(other, (int,float)):
            #тут мы возвращаем совершенно новый объект класса
            return BankAccount(self.name, self.balance+other)
        raise NotImplemented


    def __radd__(self, other):
        print('__radd__')
        return self+other
    def __mul__(self, other):
        print('метод __mul__')
        if isinstance(other, BankAccount):
            return self.balance * other.balance
        if isinstance(other, (int,float)):
            return self.balance * other
        if isinstance(other, str):
            return self.name+other
        raise NotImplemented

b= BankAccount('Ivan', 900)
r= BankAccount('Misha', 70)
print(b.balance)
print(b+12)
print(12+r)
print(b+r)
print(r*3)
print(r*'ttt')

#print(b.balance+400)#это будет работать потому что мы работаем с двумя целыми числами
#print(b+700)# не будет работать потому что два типа не поддерживают операцию сложения



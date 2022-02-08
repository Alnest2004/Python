import timeit
#__slots__ даёт 3 особенности:1) Ограничение создаваемых локальных свойств
#2)Уменьшение занимаемой памяти 3) Ускорение работы с локальными свойствами

class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def calc(self):
        self.x +=1
        del self.y
        self.y = 0

class Point2D:
    #так же уменьшает объём занимаемой памяти экземпляра класса
    __slots__ = ('x','y')#только такие имена локальных свойств мы можем создавать
    #у экземпляра класса Point2D. +Теперь отсутсвует метод pt2.__dict__
    MAX_COORD = 100
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def calc(self):
        self.x +=1
        del self.y
        self.y = 0

pt1= Point(1,2)
pt2 = Point2D(10,20)
print(pt2.x)
print(pt2.y)
print(pt2.MAX_COORD)

t1 = timeit.timeit(pt1.calc)
t2 = timeit.timeit(pt2.calc)
print(t1,t2)




#pt = Point(1,2)
#print(pt.x)
#print(pt.y)
#pt.y=100
#print(pt.y)
#pt.z = 4
#print(pt.z)
#print(pt.__dict__)
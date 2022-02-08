

class Point:
    #с помощью этого описания def куда мы записываем значения x и y сразу при создании
    #Экземлпяра класса pt = Point(5, 10)
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
        print("Создание экземпляра класса Point")

    def __del__(self):
        print("Удаление экземпляра: "+self.__str__())

    x=1; y=1
    def setCoords(self, x, y):
        self.a = x
        self.b = y

pt = Point(5, 10)
pt2 = Point(5)
pt3 = Point()
pt3 =0
print(pt.__dict__)
#Point.setCoords(pt, 5, 10) тоже самое что и ниже
pt.setCoords(5,10)#это
print(pt.__dict__)

class Rectangle:
    def __init__(self, w=0.5, h=1):
        self.width = w
        self.height = h

    def square(self):
        return self.width * self.height
 

rec1 = Rectangle(5, 2)
rec2 = Rectangle()
rec3 = Rectangle(3)
rec4 = Rectangle(h=4)
print(rec1.square())
print(rec2.square())
print(rec3.square())
print(rec4.square())

class Person:
    def __init__(self, n, s):
        self.name = n
        self.surname = s
 
 
p1 = Person("Sam", "Baker")
print(p1.name, p1.surname)
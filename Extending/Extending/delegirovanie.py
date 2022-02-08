


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y= y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

class Styles:
    def __init__(self):
        print("Конструктор Styles")
        super().__init__()#эта функция гарантирует что конструктор класса Styles и Pos
        #будут вызваны ровно 1 раз

class Pos:
    def __init__(self):
        print("Конструктор Pos")
        super().__init__()#эта функция гарантирует что конструктор класса Styles и Pos
        #будут вызваны ровно 1 раз

class Line(Styles, Pos):
    def __init__(self, sp:Point, ep:Point, color="red", width = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width
        super().__init__()

    def draw(self):
        print(f"Рисование линии: {self._sp},{self._ep}, {self._color}, {self._width}")

l = Line(Point(10,10), Point(100,100), "green", 5)
l.draw()


class Base:
    def price(self):
        return 10
class InterFoo(Base):
    def price(self):
        return super().price() * 1.1
class Discount(InterFoo):
    def price(self):
        return super().price() * 0.8

bb = Discount()
print(bb.price())

class A:
    def __init__(self):
        self.x = 10
#class B(A):
#    def __init__(self):
#        self.y = self.x + 5
# print(B().y)  # ошибка! AttributeError: 'B' object has no attribute 'x'
# правильно:
class B(A):
    def __init__(self):
        super().__init__()  # <- не забудь!
        self.y = self.x + 5
print(B().y)  # 15


class O1:
    def method(self):
        print('I am O')
class A1(O1):
    def method(self):
        super().method()
        print('I am A')
class B1(O1):
    def method(self):
        super().method()
        print('I am B')
class C1(A1, B1):
    def method(self):
        super().method()
        print('I am C')


d= C1()
d.method()
#I am O
#I am B
#I am A
#I am C
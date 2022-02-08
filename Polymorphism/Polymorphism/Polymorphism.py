# ПОЛИМОРФИЗМ - эта возможность обработки совершенно разных объектов путём использования
#одного и того же метода по названию
class Rectnatgle:

    def __init__(self, a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Rectnatgle {self.a}x{self.b}"

    def get_area(self):
        return self.a *self.b

class Square:

    def __init__(self,a):
        self.a = a

    def __str__(self):
        return f"Square {self.a}x{self.a}"

    def get_area(self):
        return self.a **2

class Circle:

    def __init__(self,r):
        self.r = r

    def __str__(self):
        return f"Circle radius={self.r}"

    def get_area(self):
        return 3.14 * self.r**2

rect1= Rectnatgle(3,4)
rect2= Rectnatgle(12,5)
#print(rect1.get_rect_area(),
#      rect2.get_rect_area())

sq1 = Square(5)
sq2 = Square(7)
#print(sq1.get_sq_area(),
#      sq2.get_sq_area())

cir1 = Circle(3)
cir2 = Circle(2)
#print(sq1.get_circle_area(),
#      sq2.get_circle_area())


figures = [rect1, rect2, sq1, sq2, cir1,cir2]
for figure in figures:
    print(figure,figure.get_area())
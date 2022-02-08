
#Если метод __bool__ не реализован то питон будет смотреть на метод __len__. Если их обоих
# нету то будет всегда выводиться True

class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __len__(self):
        print("__len__")
        return abs(self.x-self.y)

    def __bool__(self):
        print("__bool__")
        return self.x != 0 or self.y != 0


p1=Point(1,2)
p2=Point(3,4)
print(bool(Point(3,4)))
print(bool(Point(3,0)))
print(bool(Point(0,0)))
p3= Point(2,3)
if p3:
    print('hello')

p4=Point(0,0)
if p4:
    print('hello')
print(bool(p2))
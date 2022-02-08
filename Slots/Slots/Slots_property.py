#__slots__ не может нам запретить создавать новые свойства(методы) у Point2D
# Благодаря @property метод length становится типо локальным свойствам и всё равно
# __slots__ не сможет его запретить использовать
# ДОЧЕРНИЕ КЛАССЫ НЕ НАСЛЕДУЮТ КОЛЛЕКЦИЮ __SLOTS__ = ПО умолчанию так
import math
class Point2D:
    __slots__ = ('x','y', '__length')


    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.length = math.sqrt(x*x+y*y)

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

class Point3D(Point2D):
    __slots__ = 'z',#Данный метод + наследует от родительского __slots__
    #если бы тут __slots__ не был указан тогда явно он не наследуется

    def __init__(self, x,y,z):
        super().__init__(x,y)
        self.z =z


pt3= Point3D(10,20,30)

print(pt3.x, pt3.y, pt3.z)
#pt3.d = 10#не можем добавить

#pt = Point2D(1,2)
#pt3= Point3D(10,20)
#pt3.z = 30
#del pt3.x
#print(pt3.__dict__)
#pt3.x= 120#при таком присваивании благодоря методу __slots__ значение
#не будет видно если мы вызовем __dict__:
#Но присваивание пройдёт успешно
#print(pt3.x)

#print(pt.length)
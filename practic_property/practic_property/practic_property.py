
class RevealAccess():
    """Дескриптор данных, который устанавливает и возвращает значения,
       и печатает сообщение о том, что к атрибуту был доступ.
    """

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name
    
    @property
    def __get__(self, obj, objtype):
        print ('Получаю', self.name)
        return self.val

    @__get__.setter
    def __get__(self, obj, val):
        print ('Обновляю' , self.name)
        self.val = val



class CoordValue:
    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value):#причём когда вызывается этот метод параметр self
        #будет ссылаться именно на объект __value тоесть браться coordX ####
        self.__value = value

    def __delete__(self,obj):
        del self.__value

class Point:
    coordX= CoordValue()#У этих двух экземпляров создаётся переменная __value
     #в которой и хранится значение соответствуйющей координаты, то есть число
    coordY= CoordValue()#У этих двух экземпляров создаётся переменная __value
     #в которой и хранится значение соответствуйющей координаты, то есть число


    def __init__(self, x=0, y=0):
        #такие операции называются перегруженными и в действительности вызывается метод
        #__set__ у CoordValue этот метод __set__ отрабатывает и в первом случаи 
        #он записывает число х в переменную __value и на этом всё завершается
        self.coordX=x
        self.coordY=y#а когда мы выполняем эту операцию параметр self
        #будет ссылаться уже на второй объект __value тоесть браться coordY####
        # И далее в переменную __value будет занисено вот это значение =y


pt = Point(1,2)
pt.coordX = 5#БЕРЁМ ЭТО ЗНАЧЕНИЕ ИЗ КЛАССА POINT, ТО ЕСТЬ ОБРАЩАЕМСЯ К __value
print(pt.coordX, pt.coordY)

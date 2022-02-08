class CoordValue:

    def __set_name__(self,owner, name):#Этот метод вызывается автоматически при создании
        # соотв. дискриптора (CoordValue) и в параметре name хранится имя экземпляра 
        # класса. И name будет принимать значения сначала coordX, затем coordY
        print(name)
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):#instance как раз будет ссылаться на тот 
        # экземпляр класса для которого был вызван данный дескриптор
        instance.__dict__[self.__name] = value# и затем используя такую коллекцию
        # dict мы можем создать там свойство и присвоить ему определённое значение value


class Point:
    coordX= CoordValue()

    coordY= CoordValue()



    def __init__(self, x=0, y=0):

        self.coordX=x
        self.coordY=y


pt = Point(1,2)
pt2= Point(10,20)
print(pt.coordX, pt.coordY)
print(pt2.coordX, pt2.coordY)

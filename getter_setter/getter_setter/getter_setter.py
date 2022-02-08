

class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = x; self.__y = y

    #Такие методы где можно перезаписать приватные переменные
    # в ООП называются сеттерами и геттерами
    #следует проверить их тип данных. Для этого можно воспользоваться функцией
    # isinstance и записать сеттер
    """
    Обратите внимание вот на этот слеш. Он используется
   когда конструкцию в языке Python нужно записать в несколько строчек.
  Он, говорит интерпретатору языка, что следующая строчка – это продолжение первой. 
    """
    def setCoords(self, x, y):
        if (isinstance(x, int) or isinstance(x, float)) and \
            (isinstance(y, int) or isinstance(y, float)):
            self.__x = x
            self.__y = y    
        else:
            print("Координаты должны быть числами")

    def __checkValue(x):
        if isinstance(x, int) or isinstance(x, float):
           return True
        return False

    def __getattribute__(self, item):
        if item == "_Point__x":
            #Это означает получить исключение и повторно поднять его.
            raise ValueError("Private attribute")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        #мы запрещаем изменять свойство WIDTH нашего класса
        if key == "WIDTH":
            raise AttributeError
        else:
            self.__dict__[key] = value
    #Наконец, методы __delattr__ и __getattr__ можно перегрузить так:

    def __getattr__(self, item):
        print("__getattr__: "+item)
    def __delattr__(self, item):
        print("__delattr__: "+item)
    
    def getCoords(self):
        return self.__x, self.__y

pt = Point()
pt.setCoords(10, 20)
print( pt.getCoords() )
pt.setCoords("10", 20)
print( pt.getCoords() )

#мы можем изменить приватную переменную __x, так:
# pt._Point__x = 100
#и теперь она равна 100. Или, вызвать скрытый метод:
# Point._Point__checkValue(4)

"""
При необходимости мы можем осуществлять дополнительный контроль изменения атрибутов, путем перегрузки следующих методов:

__setattr(self, key, value)__ – автоматически вызывается при изменении свойства key класса;
__getattribute__(self, item) – автоматически вызывается при получении свойства класса с именем item;
__getattr__(self, item) – автоматически вызывается при получении несуществующего свойства item класса;
__delattr__(self, item) – автоматически вызывается при удалении свойства item (не важно: существует оно или нет).
"""

"""
Еще один дополнительный контроль за локальными свойствами экземпляров
классов можно сделать с помощью коллекции:

__slots__ = ["__x", "__y"]

и при попытке создать какие-либо дополнительные локальные атрибуты:

pt.z = 1

возникнет ошибка. И, обратите внимание, в slots можно указывать
имена только локальных свойств экземпляров, записать туда имена переменных
самого класса нельзя. Вот такая запись приведет к ошибке:

__slots__ = ["__x", "__y", "WIDTH"]
"""


class Person:
    def __init__(self, name):
        self.__name = name      # устанавливаем имя
        self.__age = 1          # устанавливаем возраст
 
    def set_age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")
 
    def get_age(self):
        return self.__age

         
    def get_name(self):
        return self.__name
 
    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)
         
tom = Person("Tom")
 
tom.display_info()          # Имя: Tom  Возраст: 1
tom.set_age(-3486)          # Недопустимый возраст
tom.set_age(25)
tom.display_info()          # Имя: Tom  Возраст: 25


########################################################################################
#Для создания свойства-геттера над свойством ставится аннотация @property.

#Для создания свойства-сеттера над свойством устанавливается аннотация
# имя_свойства_геттера.setter.

class Person22:
    def __init__(self, name):
        self.__name = name  # устанавливаем имя
        self.__age = 1      # устанавливаем возраст
 
    @property
    def age(self):
        return self.__age
 
    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")
     
    @property
    def name(self):
        return self.__name
         
    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)
         
         
tom22 = Person22("Tom")
 
tom22.display_info()      # Имя: Tom  Возраст: 1
tom22.age = -3486         # Недопустимый возраст
print(tom22.age)          # 1
tom22.age = 36
tom22.display_info()      # Имя: Tom  Возраст: 36
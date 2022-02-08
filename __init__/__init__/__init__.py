

#Есть три типа модификаторов доступов в Python ООП:
#
#публичный — public;
#приватный — private;
#защищенный — protected.

"""
Доступ к переменным с модификаторами публичного доступа открыт из любой точки
вне класса, доступ к приватным переменным открыт только внутри класса, и в случае
с защищенными переменными, доступ открыт только внутри того же пакета.
"""
class Cat:


    def __init__(self, name, breed='pers', age=1, color='white'):
        print('hello', self, name, breed, age, color)
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color



tom = Cat('Tom', 'siam', 40, 'black')
walt = Cat('Walt')
kelly = Cat('Kelly', age = 40)
print(kelly)
print(tom)
print(walt)
print(tom.__dict__)


class Car:
 
    # создаем атрибуты класса
    car_count = 0
 
    # создаем методы класса
    def start(self, name, make, model):
        print("Двигатель заведен")
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1

car_a = Car()  
car_a.start("Corrola", "Toyota", 2015)  
print(car_a.name)  
print(car_a.car_count)

car_b = Car()  
car_b.start("City", "Honda", 2013)  
print(car_b.name)  
print(car_b.car_count)


class Car2:
 
    @staticmethod
    def get_class_details():
        print ("Это класс Car")
 
Car2.get_class_details()

#tuple = кортеж (32,32,212,21,1)
class Square:

    @staticmethod
    def get_squares(a,b):
        return a*a, b*b

print(Square.get_squares(3,5))


class Car3:
 
    # создание методов класса
    def start(self):
        print ("Двигатель заведен")
 
car_a = Car3()  
print(car_a)

class Car4:
 
    # создание атрибутов класса
    car_count = 0
 
    # создание методов класса
    def __init__(self):
        Car4.car_count +=1
        print(Car4.car_count)

car_a = Car4()  
car_b = Car4()  
car_c = Car4()

# создаем класс Car
class Car5:  
    def start(self):
        message = "Двигатель заведен"
        return message

class Car6:  
    message1 = "Двигатель заведен"
 
    def start(self):
        message2 = "Автомобиль заведен"
        return message2
 
car_a = Car6()  
print(car_a.message1)

class Car7:  
    def __init__(self):
        print ("Двигатель заведен")
        self.name = "corolla"# ну и без подчёркиваний это глобальная переменная
        self.__make = "toyota"# с двумя подчёркиваниями это приватная переменная
        self._model = 1999#с одним подчёркиванием это защищенная переменная

car_a = Car7()  
print(car_a.name)
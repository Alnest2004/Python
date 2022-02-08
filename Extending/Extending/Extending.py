#Наследование Расширение Extending

class Person:
    age = 25

    def breathe(self):
        print('Человек дышит')

    def sleep(self):
        print('Человек спит')

    def combo(self):
        self.breathe()
        if hasattr(self, 'walk'):            
            self.walk()
        self.sleep()
        if hasattr(self, 'age'):            
            print(self.age)

class Doctor(Person):
    age = 30

    def breathe(self):
        print('Доктор дышит')

    def sleep(self):
        print('Доктор спит')

    def walk(self):
        print('Доктор идёт')

p = Person()
p.combo()
print("--")
d = Doctor()
d.combo()
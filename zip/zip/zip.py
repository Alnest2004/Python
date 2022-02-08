
#a=[5,6,7,8]
#
#b=[100,200,300,40]
#
#c='abcd'
#
#rez=zip(a,b,c)
#
#col1,col2,col3=zip(*rez)
#
#print(col1,col2,col3)


#employee_numbers = [2, 9, 18, 28]
#employee_names = ["Дима", "Марина", "Андрей", "Никита"]
#
#zipped_values = zip(employee_names, employee_numbers)
#zipped_list = list(zipped_values)
#
#print(zipped_list)

#employee_numbers = [2, 9, 18, 28]
#employee_names = ["Дима", "Марина", "Андрей", "Никита"]
#
#for name, number in zip(employee_names, employee_numbers):
#	print(name, number)
"""
Вот пример работы оператора распаковки в zip():

employees_zipped = [('Дима', 2), ('Марина', 9), ('Андрей', 18), ('Никита', 28)]
employee_names, employee_numbers = zip(*employees_zipped)

print(employee_names)
print(employee_numbers)
"""


a = [1,2,3]
b = [*a,4,5,6]
print(b) # [1,2,3,4,5,6]

def printScores(student, *scores):
   print(f"Student Name: {student}")
   for score in scores:
      print(score)
printScores("Jonathan",100, 95, 88, 92, 99)
"""
Student Name: Jonathan
100
95
88
92
99
"""

def printPetNames(owner, **pets):
   print(f"Owner Name: {owner}")
   for pet,name in pets.items():
      print(f"{pet}: {name}")
printPetNames("Jonathan", dog="Brock", fish=["Larry", "Curly", "Moe"], turtle="Shelldon")
"""
Owner Name: Jonathan
dog: Brock
fish: ['Larry', 'Curly', 'Moe']
turtle: Shelldon
"""

def test_var_args(f_arg, *argv):
    print("Первый позиционный аргумент:", f_arg)
    for arg in argv:
        print("Другой аргумент из *argv:", arg)
test_var_args('yasoob', 'python', 'eggs', 'test')


def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))
greet_me(name="yasoob",name2="dsdsds",name3="yasdsdsdsoob")


def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

args = ("two", 3, 5)
test_args_kwargs(*args)

kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)


##Если вы хотите использовать все три метода в функции, то порядок должен быть таким: 
#some_func(fargs, *args, **kwargs)

def bread(func):
    def wrapper():
        print()
        func()
        print("<\______/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print("#помидоры#")
        func()
        print("~салат~")
    return wrapper

def sandwich(food="--ветчина--"):
    print(food)

sandwich()
sandwich = bread(ingredients(sandwich))
sandwich()

@bread
@ingredients
def sandwich(food="--ветчина--"):
    print(food)

sandwich()


def decorate(funct):
    def wrapper():
        print("wrapper")
        funct()
    return wrapper

@decorate
def test():
    print("test")

test()

import someclass
def get_info(self, *args):
    return "Test data"
someclass.get_info = get_info
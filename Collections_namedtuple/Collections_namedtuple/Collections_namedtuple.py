#Каждый объект сохраненный в них может быть доступен через уникальный,
# удобный для чтения человеком, идентификатор. Это освобождает вас от
#  запоминания целочисленных индексов или выдумывания обходных путей типа
#   определения целочисленных констант как мнемоник для ваших индексов.
from collections import namedtuple
#Синтаксис namedtuple в Python
#collections.namedtuple(typename, field_names, *, 
#                      rename=False, defaults=None, module=None)

Marks = namedtuple('Marks', 'Physics Chemistry Math English')
marks = Marks(90, 85, 95, 100)
print(marks)#Marks(Physics=90, Chemistry=85, Math=95, English=100)
#В качестве второго параметра можно использовать итерируемую
# структуру данных: список, словарь, кортеж или множество.
#Если же это строка, то разные имена нужно разделить с помощью отдельного символа.

lst = ['Physics', 'Chemistry', 'Math', 'English']#Создание namedtuple с помощью списка
Marks1 = namedtuple('Marks', lst)
marks1 = Marks1(90, 85, 95, 100)
print(marks1)

#Создание namedtuple с помощью словаря
#Стартовое значение словаря — 0, поскольку значение поля игнорируется кортежем.
dct = {'Physics': 0, 'Chemistry': 0, 'Math': 0, 'English': 0}
Marks2 = namedtuple('Marks', dct)
marks2 = Marks2(90, 85, 95, 100)
print(marks2)

#Создание namedtuple с помощью кортежа
tupl = ('Physics', 'Chemistry', 'Math', 'English')
Marks3 = namedtuple('Marks', tupl)
marks3 = Marks3(90, 85, 95, 100)
print(marks3)

#Создание namedtuple с помощью множества
subject_set = {'Physics', 'Chemistry', 'Math', 'English'}
Marks4 = namedtuple('Marks', subject_set)
marks4 = Marks4(90, 85, 95, 100)
print(marks4)

#Создание namedtuple с помощью функции _make
#Функция _make также принимает итерируемый объект
# (в случае со словарем — значение).
lst = ['Physics', 'Chemistry', 'Math', 'English']
Marks5 = namedtuple('Marks', lst)
marks5 = Marks5._make([55, 78, 98, 90])
print(marks5)

#Функция _make также принимает итерируемый объект
# (в случае со словарем — значение).
marks100 = Marks5._make({55: 'Physics', 78: 'Chemistry', 98: 'Math', 90: 'English'})
print(marks100)

#Доступ к именам полей namedtuple в python
#Через смещение.
#Через точку.
#getattr().

print(marks[0])
print(marks[3])

print(marks.Physics)
print(marks.English)
#Именованные кортежи неизменяемые

#Изменение значения поля namedtuple
#Несмотря на неизменяемость есть способ, с помощью которого
# можно менять значение поля. Для этого используется функция _replace.

marks = marks._replace(Physics=99)
print(marks)
#Функция _replace() принимает имя поля и значение, которое нужно заменить,
# а возвращает именованный кортеж с измененным значением. Таким образом этот
#  тип оказывается изменяемым с помощью одного простого трюка.

Point = namedtuple('Point', ['x', 'y'])
p = Point(x=1, y=2)
print(p)
print(p.x)
print(p[0])
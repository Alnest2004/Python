

from collections import defaultdict




r =defaultdict(int)

print(r['s'])
print(r)

b=defaultdict(list, {1:[]})

b['a']=123
print(b)

b.default_factory = lambda: 'hello'#после равно указывается какое мы значение
#Хотим вернуть по умолчанию
print(b[4])
print(b)
b[5]
b[10]
print(b)



#Слаживаем оценки одинаковых фамилий
data= [
    ('ivanov', 2),
    ('petrov',1),
    ('sidorov',5),
    ('petrov',3),
    ('ivanov', 2),
    ('ivanov', 4),   
    ]

marks = defaultdict(int)#слаживаем сумму всех оценок каждого
marks_list = defaultdict(list)#Выводит список оценок каждого
marks_uniq = defaultdict(set)#Убирает повторяющиеся значения

#кортеж из 2 значений ('ivanon',2)
for surname,mark in data:
    print(surname,mark)
    marks[surname] +=mark#слаживаем сумму всех оценок каждого
    marks_list[surname].append(mark)#Выводит список оценок каждого
    marks_uniq[surname].add(mark)#Убирает повторяющиеся значения

print(marks)#слаживаем сумму всех оценок каждого
print(marks_list)#Выводит список оценок каждого
print(marks_uniq)#Убирает повторяющиеся значения





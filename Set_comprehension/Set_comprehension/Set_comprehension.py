
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
list_b = [x**3 if x < 0 else x**2 for x in list_a if x % 2 == 0]
# вначале фильтр пропускает в выражение только четные значения
# после этого ветвление в выражении для отрицательных возводит в куб, а для остальных в квадрат

#Генератор списков
#my_list = [выражение for переменная in collection]
#Генератор словарей
#my_dict = {key:value for переменная in collection}
#set = {выражение for переменная in collection}

#МОЖЕТ СОДЕРЖАТЬ ТОЛЬКО НЕИЗМЕНЯЕМЫЕ ОБЪЕКТЫ: КОРТЕЖИ. Листы не могут

my_set = {i if len(i)>4 else 'lol'  for i in ['hello', 'hi', 'hello', 'hi', 'qwerty']}
print(my_set)

my_set2= {(i,j) for i in 'aba' for j in 'def'}
print(my_set2)#НЕ УПОРЯДОЧЕННЫЙ МАССИВ ПОЛУЧАЕТСЯ+убирает повторяющиеся элементы

my_set3= [(i,j) for i in 'aba' for j in 'def']
print(my_set3)#УПОРЯДОЧЕННЫЙ МАССИВ ПОЛУЧАЕТСЯ

'''
dkfisldksk ds
]d sldpslp dls
f sfs
'''

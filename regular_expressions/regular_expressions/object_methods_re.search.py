


import re

text="<font color=#CC0000>"
match = re.search(r"(\w+)=(#[\da-fA-F]{6})\b", text)
print(match.group(1))
print(match.group(0,1,2))
print(match.groups())#возвращает кортеж из всех групп начиная с индекса 1
print(match.lastindex)#содержит индекс последней сохроняющей группы
print(match.start(1))#если нужно узнать позицию в самом тексте отчёт идёт с нуля. И в 
#скобочках указываем позицию какой группы мы ищем
print(match.end(2))#если нужно узнать конечный индекс группы
print(match.span(0))#мы можем сразу получить кортеж с начальной и конечной позицией
print(match.endpos)#определяет первый и последний(в данном примере последний)
#индекс в пределах которых осуществлялась проверка в тексте
print(match.pos)#получаем начальных индекс с которого происходил поиск
print(match.re)#возвращает скомпилированный шаблон
print(match.string)#возвращает анализируемую строку
match2 = re.search(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text)
print(match2)
print(match2.groupdict())#На выходе получим словарь из= имя группы:значение {'key': 'color', 'value': '#CC0000'}
print(match2.groupdict())
print(match2.lastgroup)#Возвращает имя последней группы. Или значение none если групп нет

#\g<name> - обращение к группе по имени;
#\1,\2,...-обращение к группе по номеру.

print(match2.expand(r"\g<key>:\g<value>"))#сформировать строку с использованием сохронённых групп

"""
МЕТОД re.search(pattern, string, flags) - ПОИСК ИМЕННО ПЕРВОГО ВХОЖДЕНИЯ
pattern-регулярное выражение(шаблон);
string- анализируемая строка;
flags-один или несколько флагов.
"""

text22 = "<font color=#CC0000 bg=#ffffff>"
#этот код будет выделять только color так как search ищет первое вхождение
match22 = re.search(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text22)
print(match22)

"""
МЕТОД re.finditer(pattern, string, flags) - ВОЗВРАЩАЕТ ИТЕРИРУЕМЫЙ ОБЪЕКТ С ПОМОЩЬЮ
КОТОРОГО МОЖНО ПЕРЕБРАТЬ ВСЕ НАЙДЕННЫЕ ВХОЖДЕНИЯ
"""

text33 = "<font color=#CC0000 bg=#ffffff>"
#этот код будет выделять все совпадения
for match33 in re.finditer(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text33):
    print(match33)

"""
МЕТОД re.findall(pattern, string, flags) - ЕСЛИ НУЖНО ПОЛУЧИТЬ СПИСОК НАЙДЕНЫХ ЗНАЧЕНИЙ
"""

#будет выводить сохроняемые значения. 
match44 = re.findall(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text33)
print(match44)
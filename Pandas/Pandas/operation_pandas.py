
import pandas as pd

a= [43,5,23,221,52,312,21,76,32,9]
data=pd.Series(a)
print(data)

print(data+2)#каждому значению прибавляется 2 И создаётся новая Series
print(data>45)#Проверит каждый элемент и выведет true или False
print(max(data))
print(min(data))
print(sum(data))
print(sorted(data))
print(tuple(data))
print(set(data))#множетсво набор уникальных элементов
b = ['hello', 'world', 'hi']#строки в pandas это Тип object
s= pd.Series(b)
print(s+s)
print(s*3)
print(s>'wkc')
print(len(data))
print(len(s))
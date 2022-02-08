
import pandas as pd
from random import randint
numbers = [randint(-50,50) for i in range(50)]
s=pd.Series(numbers)

print(s.head(20))#берём определённое количество элементов с головы
print(s.tail(20))#берём определённое количество элементов с хвоста
print(s.take([4,23,12]))#берём определённые элементы индексы которых указываем в списке!
print(s.take(range(15,35,2)))


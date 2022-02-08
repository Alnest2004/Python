import pandas as pd
from random import randint
from faker import Faker
fake = Faker()

numbers = [randint(-50,50) for i in range(15)]
names=[fake.name() for i in range(15)]
dates=[fake.date() for i in range(15)]



a=pd.Series(numbers)
ss=pd.Series(numbers, names)
print(a.sort_values())
print(a.sort_index(inplace = True))#inplace = True . Переписывает основные значения
print(ss)
print(a.sort_index(ascending=True))#ascending=True. Сортирует в алфавитном порядке
print(dates)
sup = pd.Series(numbers,dates)
print(sup.sort_index(ascending=False))


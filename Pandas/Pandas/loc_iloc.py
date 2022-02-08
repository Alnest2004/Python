
import pandas as pd
from random import randint, choice

nums = [randint(-50,50) for i in range(10)]
indexes = [choice([0,1,2,3]) for i in range(10)]
alpha = [choice('abc') for i in range(10)]


s=pd.Series(nums)
s_not=pd.Series(nums,indexes)
s_not_unique=pd.Series(nums,alpha)
#iloc мы получаем ряд под номером
print(s_not.iloc[[2,1,9]])#в этом случаи iloc нужно вызывать с [] скобками. Для передачи
#нескольких элементов нужно указать во вложенном списке [[2,1,3,4,5]]
#loc мы получаем значение по меткам(индексам)
s_not.loc[[3]] = 20#меняет все значение с индексом 3 на значение 20
print(s_not.loc[[2, 1,3]])

print(alpha)
print(s_not_unique)
print(s_not_unique.iloc[[1,3]])
print(s_not_unique.loc[['a','b']])



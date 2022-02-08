import pandas as pd
from random import randint
from faker import Faker
fake = Faker()

numbers = [randint(-50,50) for i in range(15)]
names=[fake.name() for i in range(15)]
print(names)

s=pd.Series(numbers)
print(s.sort_values())#сортирует элементы в порядке возрастания. Этот метод создаёт новый
#Series

print(s.sort_values(inplace=False))#inplace - если True, тогда меняет значения основного элемента
#тоесть переписываются значения, а не создаётся новый

print(s.sort_values(ascending= False))#Порядок сортировки, если False то от большего к меньшего
# в порядке убывания 

n= pd.Series(names)
print(n.sort_values(ascending=False))#Если False, то сортировка с конца алфавита Z-A


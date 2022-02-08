import pandas as pd
from random import randint
from faker import Faker
fake = Faker()

numbers = [randint(-50,50) for i in range(75)]
names=[fake.name() for i in range(15)]

def sign(x):
    if x>0:
        return 'Positive'
    if x<0:
        return 'Negative'
    return 'Zero'

def surname(s):
    return s.split()[1]#указываем[0] какой элемент после разбиения пробелами мы берём

a=pd.Series(numbers)
ss=pd.Series(names)
print(ss)
print(ss.apply(lambda s:s.split()[1]))
print(ss.apply(lambda s:len(s)))


print(a.apply(sign).tail(10))#нужно писать sign Без скобок. И этот метод будет вызываться к каждому 
#элементу

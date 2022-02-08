
import pandas as pd
from random import randint, shuffle
from string import ascii_lowercase

numbers = [randint(-50,50) for i in range(26)]
s=pd.Series(numbers)
print(len(s))
print(s[::-1])

ind = list(ascii_lowercase)
shuffle(ind)#перемешиваем все буквы алфавита
print(ind)

letters=pd.Series(numbers,ind)
print(letters['a':'b'])#и первый и послежний элемент будут включаться
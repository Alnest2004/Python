
import pandas as pd
df3 = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]
})
df3.index = ['KZ', 'RU', 'BY', 'UA']
df3.index.name = 'Country Code'

df3.to_csv('filename.cvs')

df = pd.read_csv('filename.cvs', sep=',')
print(df)
print('-'*100)
"""
DataFrame.groupby(by=None, axis=0, level=None,
as_index=True, sort=True, group_keys=True, squeeze=NoDefault.no_default,
observed=False, dropna=True)

by : mapping, function, label, or list of labels
axis: {0 or ‘index’, 1 or ‘columns’}, default 0
"""
titanic_df = pd.read_csv('titanic.csv')
print(titanic_df.head(20))
#Необходимо подсчитать, сколько женщин и мужчин выжило, а сколько нет. 
#В этом нам поможет метод .groupby.
print(titanic_df.groupby(['Sex', 'Survived'])['PassengerID'].count())
#А теперь проанализируем в разрезе класса кабины:
print('-'*100)
print(titanic_df.groupby(['PClass', 'Survived'])['PassengerID'].count())

#new_list = [expression for member in iterable (if conditional)]
#prices = [i if i > 0 else 0 for i in original_prices]
"""
def get_price(price):
    return price if price > 0 else 0
prices = [get_price(i) for i in original_prices]
#prices
#[1.25, 0, 10.22, 3.78, 0, 1.16]
"""
matrix = [[1, 2], [3,4], [5,6], [7,8]]
tra=[[row[i] for row in matrix] for i in range(2)]
print(tra)

#В нашем примере set comprehension выводит все уникальные элементы
quote = "life, uh, finds a way"
unique_vowels = {i for i in quote if i in 'aeiou'}
print(unique_vowels)
#{'a', 'e', 'u', 'i'}

#Dictionary comprehensions аналогично, с дополнительным требованием определения ключа:
squares = {i: i * i for i in range(10)}
print(squares)
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

#Интерпретатор Python хранит значение последнего выражения в специальной переменной «_»
matrix = [[i for i in range(5)] for _ in range(6)]
print(matrix)

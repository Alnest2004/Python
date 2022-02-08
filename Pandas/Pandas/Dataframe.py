

import pandas as pd

df = pd.DataFrame({
    'name': ['alice','bob','charlie','david'],
    'age': [25,26,27,22],
})

# each element of the age column is a string
# so you can call .upper() on it
df['name_uppercase'] = df['name'].apply(lambda element: element.upper())
print(df)
print('-'*100)

df1 = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]
})
print(df1)
print('-'*100)

#Индекс по строкам можно задать разными способами, например, при
# формировании самого объекта DataFrame или "на лету":
df2 = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]
}, index=['KZ', 'RU', 'BY', 'UA'])
print(df2)
print('-'*100)

df3 = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]
})
df3.index = ['KZ', 'RU', 'BY', 'UA']
df3.index.name = 'Country Code'
print(df3)
print('-'*100)

print(df3['country'])
print('-'*100)
#.loc - используется для доступа по строковой метке
#.iloc - используется для доступа по числовому значению (начиная от 0)
print(df3.loc['KZ'])
print('-'*100)

print(df3.iloc[0])
print('-'*100)

#Можно делать выборку по индексу и интересующим колонкам:
print(df3.loc[['KZ', 'RU'], 'population'])#сначала указываем строку(по умолчанию от 0..)
#а потом столбец
print('-'*100)

print(df3.loc['KZ':'BY', :])
#Фильтровать DataFrame с помощью т.н. булевых массивов:
print('-'*100)
print(df3[df3.population > 10][['country', 'square']])
print('-'*100)
df3['density'] = df3['population'] / df3['square'] * 1000000
print(df3)
print('-'*100)

#Переименовывать столбцы нужно через метод rename:
df3 = df3.reset_index('Country Code')
df3 = df3.rename(columns={'Country Code': 'country_code'})
print(df3.loc[[1]])#ЕСЛИ убрать сброс индексов(reset_index) Тогда можно указывать 
# строку с помощью df3.loc[['RU']]
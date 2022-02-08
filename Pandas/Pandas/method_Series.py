
import pandas as pd

names=['Kevin', 'Jack', 'Bob', 'Robin']
numbers = [10,-20,50,-30,40, ]
s=pd.Series(names)
nums = pd.Series(numbers)
print(nums)

print(nums.sum())
print(nums.max())
print(nums.product())
print(pd.Series([1,2,3]).product())
print(nums.mean())
print(s.sum())
print(s.max())
print(s.min())
print(nums.lt(11))#сравнивает тоже самое что и nums<11
print(nums.gt(15))#сравнивает тоже самое что и nums>15
print(nums.eq(50))#сравнивает на равно
print(nums.ne(50))#сравнивает на не равно
print(nums.ge(50))#больше или равно
print(nums.le(50))#меньше или равно
print(nums.abs())






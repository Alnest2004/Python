import pandas as pd

names=['Bob','Jack', 'Kevin', 'Robin']
letters ='b','j','k','r'
numbers = [10,20,30,40,50]

s=pd.Series(names)
s_letters =pd.Series(names,index = letters)
nums =pd.Series(numbers)
print(s.values)
print(nums.values)

print(s.index)
print(s_letters.index)

print(s_letters.size)
print(nums.is_monotonic)

print(nums.size)

print(nums.ndim)


import pandas as pd

a=[54,3,4,2,33]
b=[True, False, True]
s = pd.Series(b)
print(s[2])
v= pd.Series(a)
print(v[4])
ss=pd.Series(range(10,100,10))
print(ss)
suk = ['hello', 'world','messi']
r= pd.Series(suk,['привет', 'мир', 'a'])
print(r)
print(r['привет'])
d={'привет':'hello', 'мир':'world','messi':'best'}
t=pd.Series(d)
print(t['messi'])
print(pd.Series(list('world')))#если не поставить лист то world будет целым словом
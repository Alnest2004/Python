
s='hello'
d={}
#f = open('123.txt')
try:
    1/0
except (KeyError, IndexError):
    print('ERROR LOOKUP')
except ZeroDivisionError:
    print('ZeroDivisionError')
else:# ELSE МОЖЕТ ПИСАТЬСЯ ТОГДА КОГДА ЕСТЬ EXCEPT
    print('GOOD')
finally:
    print('end')
    #f.close()


    
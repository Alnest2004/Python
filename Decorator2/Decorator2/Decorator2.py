
#wraps
from functools import wraps

def table(func):

    @wraps(func)
    def inner(*args,**kwargs):
        print('<table>')
        func(*args,**kwargs)
        print('</table>')

    return inner

def say():
    print('hello world')

def sqr(x):
    """
    функция возводит в квадрат x
    """
    print(x**2)

print(sqr.__doc__)


###################
def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
   """does some math"""
   return x + x * x

print(f.__name__)  # prints 'f'
print(f.__doc__)   # prints 'does some math'
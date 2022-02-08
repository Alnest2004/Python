#decorator


def header(func):

    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')
    return inner

def table(func):

    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')
    return inner

@table
@header # say= table(header(say))
def say(name, surname, age):
    print('hello!',name, surname,age)


say('vasya', 'Ivanov', 30)

def decorator_function(func):
    def wrapper():
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func()
        print('Выходим из обёртки')
    return wrapper

@decorator_function
def hello_world():
    print('Hello world!')

hello_world()

def decorator(func):
    '''Основная функция'''
    print('декоратор')
    def wrapper():
        print('-- до функции', func.__name__)
        func()
        print('-- после функции', func.__name__)
    return wrapper

@decorator
def wrapped():
    print('--- обернутая функция')

print('- старт программы...')
wrapped()
print('- конец программы')

def decorator_1(func):
    print('декоратор 1')
    def wrapper():
        print('перед функцией')
        func()
    return wrapper

def decorator_2(func):
    print('декоратор 2')
    def wrapper():
        print('перед функцией')
        func()
    return wrapper

@decorator_1
@decorator_2 #basic_1= decorator_1(!!!decorator_2(basic_1)!!!) --- первое будет
#выполняться то что внутри воскл. знаков
def basic_1():
    print('basic_1')

@decorator_1
def basic_2():
    print('basic_2')

print('>> старт')
basic_1()
basic_2()
print('>> конец')



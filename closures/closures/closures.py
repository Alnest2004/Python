# Замыкания
# В результате nonlocal будет изменяться переменная ближайшей
#  объемлющей функции, в нашем случае – функции Fn2().
# Инструкция nonlocal

# Несколько объемлющих функций

def Fn1():
    # эта переменная не изменяется из функции Fn3(),
    # потому что ее перекрывает переменная из функции Fn2()
    x1 = 25

    def Fn2():
        x1 = 33 # эта переменная будет изменяться в функции Fn3()

        def Fn3():
            nonlocal x1
            x1 = 55 # Fn2.x1 = 55

        Fn3()
        print('Fn2.x1 = ', x1)

    Fn2()
    print('Fn1.x1 = ', x1)

Fn1()

"""
Результат выполнения программы

Fn2.x1 = 55
Fn1.x1 = 25
Если в теле функции Fn2() убрать строку x1 = 33, то изменяться будет значение переменной x1 функции высшего уровня, то есть функции Fn1(). В этом случае программа выдаст результат

Fn2.x1 = 55
Fn1.x1 = 55
"""

def counter():
    count = 0
    def inner():
        nonlocal count
        count +=1
        return count
    return inner

q=counter()
print(q())
print(q())
r= counter()
print(r())
print(r())
print(r())


#def adder(value):
#    def inner(a):
#        return value+a
#
#    return inner
#
#a2=adder(2)
#b=a2(5)
#print(b)
#
#a5=adder(5)
#bb=a5(10)
#print(bb)

G = 10

def make_closure():
    a = 1
    b = 2
    def inner(x):
        return x + G + a
    return inner
b=make_closure()
print(b(5))

def make_closure():
    y = 1
    def inner(x):
        return x + y
    y = 42
    return inner
print(make_closure()(100))


printers = []
for i in range(10):
    def printer():
        print(i)
    printers.append(printer)

printers[0]()
printers[5]()
printers[9]()
i = 42
printers[0]()
"""
Здесь тоже фактическое запоминание происходит при выходе
из области видимости в которой определена переменная i,
вот только эта область видимости на момент вызова замыканий 
ещё не завершилась
Поэтому после выхода из цикла все замыкания выводят 9,
а после изменения значения переменной i выводимое значение
также меняется!
"""
#Как же запоминать то, что нужно и когда нужно?
#нужно замкнуть переменную в области видимости,
# которая завершится сразу же после создания замыкания!
#  Этого можно добиться, завернув создание функции в… другую функцию!
printers = []
for i in range(10):
    def make_printer(arg):
        def printer():
            print(arg)
        return printer
    p = make_printer(i)
    printers.append(p)

printers[0]()
printers[5]()

def mul(a):
        def helper(b):
            return a * b
        return helper
mul(5)(2)#10

new_mul5 = mul(5)
new_mul5(2)#10

def fun1(a):
        x = a * 3
        def fun2(b):
            nonlocal x
            return b + x
        return fun2

test_fun = fun1(4)

test_fun(7)#19

def get_candy():
    candy = 5
    def increment_candy(): 
        nonlocal candy
        candy += 1
        return candy
    return increment_candy
    
result = get_candy()()
print('Всего {} конфет.'.format(result))#Всего 6 конфет

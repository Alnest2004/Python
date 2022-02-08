

try:
    raise ValueError('ошибка Значения')
except ValueError as first:
    try:
        raise TypeError('ошибка типа')
    except TypeError as second:
        raise Exception('BIG BOY') from first


#try:
#    [1,2,3][15]
#except(KeyError, IndexError) as error:
#    print(f"Logging error:{repr(error)}")
#    raise TypeError('ошибка типа') from None#если написать from None выдаст ласт ошибку
#except ZeroDivisionError as err:
#    print('ZeroDivisionError')
#    print(f"Logging error: {err} {repr(err)}")


print('hello1')
print('hello2')
print('hello3')
try:#попытаться сделать
    a=int(input())
except:
   raise ValueError('Неправильное значение, передавайте число')# указывает название или тип ошибки которую ловим


#f = open('1.txt')
#ints = []
#try:
#    for line in f:
#       ints.append(int(line))
#except ValueError:
#    print('Это не число. Выходим.')
#except Exception:
#    print('Это что ещё такое?')
#else:
#   print('Всё хорошо.')
#finally:
#    f.close()
#    print('Я закрыл файл.')
    # Именно в таком порядке: try, группа except, затем else, и только потом finally.

#Это не число. Выходим.
#Я закрыл файл.

#повторять цикл до тех пор пока всё пройдёт без ошибки

while True:
    try:
        num = int(input())
        print(num)
        break
    except:
        print("Это не число")
print("Вы ввели число!", num)


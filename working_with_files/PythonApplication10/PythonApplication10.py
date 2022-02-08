
import os
path='E:\\САЙТ'

def obxodFile(path, name, level=1):
    print('Level=', level,'Content:', os.listdir(path))
    for i in os.listdir(path):
        if name==i:
            print('ПОЗДРОВЛЯЮ НАШЛИ! снизу ======================================')
        if os.path.isdir(path+'\\'+i):
            print('Спуск', path+'\\'+i)
            obxodFile(path+'\\'+i, name, level+1)
            print('Возвращаемся в', path)


obxodFile(path,'clients')
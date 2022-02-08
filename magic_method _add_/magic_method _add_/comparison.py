
"""
__eq__(self, other)
Определяет поведение оператора равенства, ==.

__ne__(self, other)
Определяет поведение оператора неравенства, !=.

__lt__(self, other)
Определяет поведение оператора меньше, <.

__gt__(self, other)
Определяет поведение оператора больше, >.

__le__(self, other)
Определяет поведение оператора меньше или равно, <=.

__ge__(self, other)
Определяет поведение оператора больше или равно, >=.

"""

"""
класс-декторатор в модуле functools, который и определит все сравнивающие методы,
от вас достаточно определить только __eq__ и ещё один (__gt__, __lt__ и т.п.) Эта
возможность доступна начиная с 2.7 версии Питона, но если это вас устраивает, вы
сэкономите кучу времени и усилий. Для того, чтобы задействовать её, поместите
@total_ordering над вашим определением класса.
"""

class Word(str):
    '''Класс для слов, определяющий сравнение по длине слов.'''

    def __new__(cls, word):
        # Мы должны использовать __new__, так как тип str неизменяемый
        # и мы должны инициализировать его раньше (при создании)
        if ' ' in word:
            print ("Value contains spaces. Truncating to first space.")
            word = word[:word.index(' ')] # Теперь Word это все символы до первого пробела
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)

a=Word('foo')
b=Word('bar')
print(a==b)

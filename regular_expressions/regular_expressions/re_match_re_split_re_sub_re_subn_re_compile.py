
import re

text="<font color=#CC0000>"
match = re.search(r"(\w+)=(#[\da-fA-F]{6})\b", text)
print(match.group(1))

"""
МЕТОД re.findall(pattern, string, flags) - ОПРЕДЕЛЯЕТ СОВПАДЕНИЕ ШАБЛОНА pattern в начале
строки string с учётом флагов flags.
pattern-регулярное выражение(шаблон);
string- анализируемая строка;
flags-один или несколько флагов.
"""
#что бы скобочки работали как поиск этих скобок внутри текста нужно указать
#перед скобками чёрточку \(...\)

text = "+7(123)456-78-90"
#ищет совпадение с самого начала строки. Если перед + будет пробел, то уже не найдёт
m=re.match(r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}", text)
print(m)

"""
МЕТОД re.split(pattern, string, flags) - ВЫПОЛНЯЕТ РАЗБИВКУ СТРОКИ string по заданному
шаблону pattern
pattern-регулярное выражение(шаблон);
string- анализируемая строка;
flags-один или несколько флагов.
"""

text ="""<point lon="40.8482" lat="52.6274" />
<point lon="40.5221" lat="52.6212274" />; <point lon="40.213" lat="52.2121" />
<point lon="40.312" lat="52.212" />, <point lon="40.212" lat="52.62731214" />
"""
#[\n;,] - указываются символы по которым можно разделить. \n это перенос строки 
# + Значит что этих символов может быть несколько
ar=re.split(r"[\n;,]+",text)
print(ar)

"""
МЕТОД re.sub(pattern, repl, count, flags) - ВЫПОЛНЯЕТ ЗАМЕНУ В СТРОКЕ string найденных 
совпадений с строкой repl или результатам работы функции и возвращает преобразованную строку
pattern-регулярное выражение(шаблон);
repl - строка или функция для замены найденного выражения;
string- анализируемая строка;
count - максимальное число замен(если не указано, то неограниченно);
flags-один или несколько флагов(по умолчанию не используются).
"""

text22 = """Москва
Казань
Тверь
Самара
Уфа"""
# \s* - могут быть пробельные символы 
#  r"<option>\1</option>\n" - тут говорим как будем преобразовывать строку мы тут обращаемся
# к сохроняющей группе \1 и говорим что до него и после него будет идти тег option 
# и перенос строки
list = re.sub(r"\s*(\w+)\s*", r"<option>\1</option>\n", text22)
print(list)

count = 0
def replFind(m):
    global count
    count += 1
    return f"<option value='{count}'>{m.group(1)}</option>\n"

list100 = re.sub(r"\s*(\w+)\s*", replFind, text22)
print(list100)

"""
МЕТОД re.subn(pattern, repl, count, flags) - ВЫПОЛНЯЕТ ЗАМЕНУ В СТРОКЕ string найденных 
совпадений с строкой repl или результатам работы функции и возвращает преобразованную строку
и ЧИСЛО ПРОИЗВЕДЁННЫХ ЗАМЕН
pattern-регулярное выражение(шаблон);
repl - строка или функция для замены найденного выражения;
string- анализируемая строка;
count - максимальное число замен(если не указано, то неограниченно);
flags-один или несколько флагов(по умолчанию не используются).
"""

list200, total = re.subn(r"\s*(\w+)\s*", r"<option>\1</option>\n", text22)
print(list200, total)

"""
МЕТОД re.compile(pattern, flags) - ВЫПОЛНЯЕТ КОМПИЛЯЦИЮ РЕГУЛЯРНОГО ВЫРАЖЕНИЯ И ВОЗВРАЩАЕТ
ЕГО В ВИДЕ ЭКЗЕМПЛЯРА КЛАССА pattern

Pattern содержит свойства:
flags - возвращает список флагов, которые были установлены при компиляции
pattern - строка исходного шаблона
groupindex - словарь, ключами которого являются имена сохрарняющих групп, а значениями
- номера групп(пустой, если имена не используются).
"""

rx=re.compile(r"\s*(\w+)\s*")#тут мы скомпилировали шаблон заранее и затем его использовали
#через rx.
list999,total555= rx.subn(r"<option>\1</option>\n", text22)
list888 = rx.sub(replFind, text22)
print(list999, total555, list888, sep="\n")
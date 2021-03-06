

import re
#\bслово\b - в этом случаи будет выводиться только в том случаи если это слово
#одно целиком, без вхождений в другое слово

#для регулярных выражений доступны следующие проверки:
"""
^ - начало текста(с флагом re.MULTITLE - начало строки)
$ - Конец текста(с флагом re.MULTITLE - позиция перед символом переноса строки \n)
\A - начало текста
\b - Граница слова(внутри символьных классов [] соответсвует символу BACKSPACE)
\B - Граница не слова(зависим от флага re.ASCII)
\Z - Конец текста
(?=exp) - Проверка на совпадение с выражением exp продолжения строки.
При этом позиция поиска не смещается на выражение exp(опережающая проверка).
(?!exp) - Проверка на несовпадение с выражением exp продолжения строки.(Также опережающая
проверка).
(?<=exp) - Проверка на совпадение с выражением exp хвоста уже обработанной(проверенной)
строки.
(?<!exp) - Проверка на несовпадение с выражением exp хвоста уже обработанной(проверенной)
строки.
"""

text = "подоходный налог"
text1= """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1251">
<meta name="viewport" content="width=device-width, inital-scale=1.0">
<title>Уроки по Python</title>
</head>
<body>
<p align=center>Hello World!</p>
</body>
</html>"""

match = re.findall(r"\b(прибыль|обретение|доход)\b", text)
#?=</script> - БУДЕМ ИСКАТЬ ПО ШАБЛОНУ СОВПАДЕНИЕ ПОКА НЕ ВСТРЕТИМ ТАКУЮ ЗАПИСЬ </script>
#ИСПОЛЬЗУЕМ \w\W вместо . потому что . не включает перенос строки
#?<! - если в конце выделяемых данных появляется пробел или символ табуляции
#то мы останавливаемся и то что получилось то и идёт в значение этого атрибута
#(простыми словами пробел просто удаляется в конце)

#(?P<q>[\"'])? - ласт вопрос означает что данная группа может присутствовать а может и нет
#то есть кавычка  может быть а может и не быть
#(?(q)([^\"']+(?<![ \t])) - если кавычка присутствовала, то мы выполняем вот этот шаблон
#([^ \t>]+)) - если кавычка не присутствовала, то мы выполняем вот этот шаблон

#Нужно это для того что бы и отыскивало вот такие атрибуты align=center

match2 = re.findall(r"""([-\w]+)    #выделяем атрибут
                    [ \t]*=[ \t]*
                    (?P<q>[\"'])?
                    (?(q)([^\"']+(?<![ \t]))|([^ \t>]+))""",
                   text1, re.MULTILINE|re.VERBOSE)
# | ЭТО ОПЕРАЦИЯ ИЛИ 
# re.VERBOSE благодаря этому мы можем писать комментарии

"""
(?flags), где flags - Один или несколько флагов:
a-то же самое, что и re.ASCII;
i - соответствует re.IGNORECASE;
m-для re.MULTILINE;
s - для re.DOTALL;
x - для re.VERBOSE.
"""
print(match2)

text100="Python, python, PYTHON"
match100=re.findall(r"(?im)python", text100)
print(match100)
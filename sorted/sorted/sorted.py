
#sort-метод списка vs sorted-встроенная функция
a=[4,-10,43,-300,54,89,-34]

b='hello world'
c=('hi', 'zero', 'abracadabra', 'pikachu')

c=sorted(c, reverse=True)
print(c)

"""
Ещё одно отличие заключается в том, что метод list.sort() определён только для списков, 
в то время как sorted() работает со всеми итерируемыми объектами:

sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
[1, 2, 3, 4, 5]
Если вам нужны их значения или пары «ключ-значение», используйте методы
dict.values() и dict.items() соответственно.
"""

aa=sorted("This is a test string from Andrew".split(), key=str.lower)
print(aa)

student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
    ]

cc=sorted(student_tuples, key=lambda student: student[2]) 
print(cc)

"""
Тот же метод работает для объектов с именованными атрибутами:

class Student:
        def __init__(self, name, grade, age):
            self.name = name
            self.grade = grade
            self.age = age
        def __repr__(self):
            return repr((self.name, self.grade, self.age))
        def weighted_grade(self):
            return 'CBA'.index(self.grade) / self.age

student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
    ]
sorted(student_objects, key=lambda student: student.age)   # сортируем по возрасту
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
"""

"""
decorated = [(student.grade, i, student) for i, student in enumerate(student_objects)]
decorated.sort()
[student for grade, i, student in decorated]               # раздекорируем
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
"""
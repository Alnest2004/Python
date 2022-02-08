


class DepartmentIT:
    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_DEV = 2

    #1 метод
    def info(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    #2 метод
    def info2(self):
        print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.REACT_DEV)
    #3 метод
    @property
    def info_prop(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)
    
    #4 метод
    @classmethod
    def info_class(cls):#cls- это сам класс. self- экземпляр класса
        print(cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV)

    #5 метод
    @staticmethod
    def info_static():
        print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.REACT_DEV)

    def hiring_pyt_dev(self):
        self.PYTHON_DEV = self.PYTHON_DEV+1 #Добавится локальная переменная но первоночальная 
        #запись не изменится, что бы её изменить нужно написать так:
        DepartmentIT.PYTHON_DEV = DepartmentIT.PYTHON_DEV+1

it1 = DepartmentIT()
print(it1.PYTHON_DEV)
it1.hiring_pyt_dev()
print(it1.PYTHON_DEV)
print(DepartmentIT.PYTHON_DEV)


it1.info()
it1.info2()
it1.info_prop
it1.info_class()
it1.info_static()

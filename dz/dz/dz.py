
class Calendar:

    __slots__ = ['_day', '_months', '_year']#Добавить к экземпляру новых с
    #войст которые не перечислены тут в атрибуте __slots__ будет нельзя, будет 
    #вызвано исключение

    def __init__(self,day,months,year):
        self._day = day
        self._months = months
        self._year = year


    @property#ЭТО ГЕТТЕР ОН НУЖЕН ДЛЯ ПОЛУЧЕНИЯ ЗНАЧЕНИЯ ИНКАПСУЛИРОВАНОГО СВОЙСТВА
    def data(self):
        print("Вывод информации")
        print(self._day, self._months, self._year)

    @data.setter
    def data(self,day,months,year):
        self._day = day
        self._months = months
        self._year = year


test = Calendar("22", "09", "1998")
test.data

test._day=55
test.data






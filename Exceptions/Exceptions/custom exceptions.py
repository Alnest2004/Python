class ExceptionPrint(Exception):
    """"""


class ExceptionPrintSendData(ExceptionPrint):
    def __init__(self,*args):
        super().__init__(*args)
        self.msg = args[0] if args else None

    def __str__(self):
        return f"Ошибка: {self.msg}"


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"печать: {str(data)}")

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData("принтер не отвечает")

    def send_to_print(self,data):
        return False

p = PrintData()
try:
    p.print("123")
#сработает этот except потому что он первым и подойдёт
except ExceptionPrintSendData as e:#выведет "Ошибка: принтер не отвечает"
    print(e)
except ExceptionPrint:
    print("Ошибка печати")
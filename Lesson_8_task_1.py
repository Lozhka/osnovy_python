"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

class Data:
    @classmethod
    def number(cls, data):
        valid = cls.validation(data)
        my_list = []
        for i in valid:
            my_list.append(int(i))
        print(my_list)

    @staticmethod
    def validation(data):
        data_list = data.split("-")
        if int(data_list[0]) > 31:
            print("дата не может быть > 31")
        if int(data_list[1]) > 12:
            print("месяц не может быть > 12")
        if int(data_list[2]) > 2020:
            print("год не может быть > 2020")
        return data_list


my_data = Data()
my_data.number("04-04-1995")

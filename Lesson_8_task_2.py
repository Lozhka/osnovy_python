"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


print("---Деление---")
num_1 = input("Введите первое число: ")
num_2 = input("Введите второе число: ")

try:
    num_1, num_2 = int(num_1), int(num_2)
    if num_2 == 0:
        raise OwnError("Деление на ноль!")
except ValueError:
    print("Вы ввели не число.")
except OwnError as o_e:
    print(o_e)
else:
    print(f"{num_1} / {num_2} = {num_1 / num_2}")

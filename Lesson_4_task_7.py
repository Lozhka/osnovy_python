# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.

from math import factorial
from itertools import count

def fib_gen():
    for el in count(1):
        yield factorial(el)

x = 0
for i in fib_gen():
    print('Factorial {} - {}'.format(x + 1, i))
    if x == 14:
        break
    x += 1
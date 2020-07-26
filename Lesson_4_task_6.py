# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

# a

from itertools import count, cycle

for i in count(int(input('Введите стартовое число: '))):
    print(i)

# b

from itertools import count, cycle

i = 0
for el in cycle(["1", '2', '3']):
    if i > 4:
        break
    print(el)
    i += 1
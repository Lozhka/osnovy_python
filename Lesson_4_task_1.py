# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.

import sys

hours, money_per_hour, bonus = map(float, sys.argv[1:])
print('Зарплата сотрудника - {}'.format(hours * money_per_hour + bonus))

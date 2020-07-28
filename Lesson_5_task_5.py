# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.

with open ('task5.txt', 'w', encoding='utf8') as f:
    nums = input('Введите целые числа через пробел: ')
    f.write('Введеные числа: ' + nums + '\n')
    nums = map(int, nums.split())
    sum_nums = sum(nums)
    f.write('Сумма чисел: ' + str(sum_nums))
    print('Сумма введенных чисел: ', sum_nums)
print('Все записано в файл.')

# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

my_list = [1, 23, 32, 45, 46, 68, 87, 90]
new_list = [num for i, num in enumerate(my_list) if my_list[i] > my_list[i - 1] and i != 0]
print(new_list)
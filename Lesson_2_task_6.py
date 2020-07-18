# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.

my_list = []
my_dict = {}

name_input = ''
price_input = ''
quantity_input = ''
units_input = ''
output = ''
n = 1
while output != 'q':
    name_input = input('Введите название товара: ')
    while name_input == '':
        name_input = input('Введите название товара: ')

    Input = False
    while not Input:
        price_input = input('Укажите стоимость товара: ')
        for i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if i in price_input:
                Input = True
                break
    price_input = int(price_input)

    Input = False
    while not Input:
        quantity_input = input('Введите количество: ')
        for i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if i in quantity_input:
                Input = True
                break
    quantity_input = int(quantity_input)

    units_input = input('Введите единицы измерения: ')
    while units_input == '':
        units_input = input('Введите единицы измерения: ')

    output = input('Чтобы выйти введите "q", чтобы продолжить "enter": ')

    my_dict_tuple = {}
    my_dict_tuple.update({'название': name_input, 'цена': price_input, 'количество': quantity_input, 'eд': units_input})
    my_tuple = (n, my_dict_tuple)
    my_list.append(my_tuple)
    n += 1
    print('---------------------------------')  # Завершение цикла ввода данных

name = []
price = []
quantity = []
units = []

for i in range(len(my_list)):
    name.append(my_list[i][1].get('название'))
    price.append(my_list[i][1].get('цена'))
    quantity.append(my_list[i][1].get('количество'))
    units.append(my_list[i][1].get('eд'))

units = list(set(units))

my_dict.update({'Название': name, 'Цена': price, 'Количество': quantity, 'Ед': units})

print(f'Вывод аналитики\n---------------------------------')
for key, value in my_dict.items():
    print(f'{key}: {value}')
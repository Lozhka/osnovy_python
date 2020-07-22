def numbers_division():
    try:
        x = int(input('Введите первое число: '))
        y = int(input('Введите второе число: '))
        print(f'{x} / {y} = {x / y}')
    except ZeroDivisionError:
        print('Нельзя делить на ноль!')
    except ValueError:
        print('Error!')


numbers_division()
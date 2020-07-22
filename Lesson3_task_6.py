def int_func():
    while True:
        words = input('Введите слова через пробел или "Q" для выхода: ')
        if 'Q' in words and len(words) < 2:
            break
        for i in words:
            i = ord(i)
            if i != 32 and i < ord("a") or i > ord("z"):
                print('Вы ввели неправильно, попробуйте еще раз.')
                break
        else:
            print(words.title())


int_func()
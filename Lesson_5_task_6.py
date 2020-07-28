# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий

import re

try:
    with open('lab.txt', encoding='utf-8') as file:
        my_dict = {}
        my_list = []
        for line in file:
            my_list = re.findall('\\b\\d+\\b', line)
            names = re.findall(r'\w+', line)
            for i, item in enumerate(my_list):
                my_list[i] = int(item)
            my_list = sum(my_list)
            my_dict[names[0]] = my_list
        print(f'Лаборатные и практические:\n{my_dict}')
except IOError:
    print('An I / O error has occurred!')

# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.

with open('task_4.txt', encoding = 'utf8') as f:
    lines = f.readlines()

with open('task_44.txt', 'w', encoding = 'utf8') as f:
    for line in lines:
        if '1' in line:
            line = line.replace('One', 'Один')
        elif '2' in line:
            line = line.replace('Two', 'Два')
        elif '3' in line:
            line = line.replace('Three', 'Три')
        elif '4' in line:
            line = line.replace('Four', 'Четыре')
        f.write(line)

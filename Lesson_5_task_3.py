# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open('text2.txt', encoding='utf-8') as f:
    salaries = []
    lines = f.readlines()
    for line in lines:
        name, salary = line.split(' - ')
        salaries.append(int(salary))
        if int(salary) < 20000:
            print(line, end = '')
    print('\nСредняя зарплата: ', sum(salaries) / len(salaries))

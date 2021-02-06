# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open('text_6.txt', 'r', encoding='utf-8') as read_file:
    dict = {el.split(':')[0]: [el.split(':')[1].split()[0], el.split(':')[1].split()[1], el.split(':')[1].split()[2]]
            for el in read_file.readlines()}

for key in dict:
    sum = 0
    for el in dict[key]:
        if len(el) > 1:
            sum += int(el.split('(')[0])
    dict[key] = sum

print(dict)

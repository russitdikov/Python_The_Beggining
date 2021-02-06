# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со
# средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json

f_list = []
with open('text_7.txt', 'r', encoding='utf-8') as read_file:
    f_dict = {el.split()[0]: (float(el.split()[2]) - float(el.split()[3])) for el in read_file.readlines()}
profit_c = 0
f_count = 0
for key in f_dict:
    if f_dict[key] > 0:
        profit_c += f_dict[key]
        f_count += 1
f_list.append(f_dict)
f_list.append({'avarage_profit': profit_c / f_count})

with open('l5_HT_7.json', 'w', encoding='utf-8') as f_export:
    json.dump(f_list, f_export, ensure_ascii=False, )

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.

with open('text_3.txt', 'r', encoding='utf-8') as h_t_3:
    line = h_t_3.readlines()
staff_dic = {el.split()[0]: float(el.split()[1]) for el in line}
less_than_20k = [staff for staff in staff_dic if staff_dic.get(staff) < 20000]
c_staff=0
salary=0
for staff in staff_dic:
    c_staff +=1
    salary += staff_dic.get(staff)

print(f'Сотрудники с заработной платой ниже 20000: {less_than_20k}')
print(f'среднаяя заработная плата на предприятии {salary/c_staff}')

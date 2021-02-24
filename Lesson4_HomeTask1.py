# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
# платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах * ставка в час)
# + премия. Для выполнения расчета для конкретных значений необходимо
# запускать скрипт с параметрами.

from sys import argv
def s_calc():
    try:
        script_name, workhours, s_per_hour, bonus = argv
        print((float(workhours) * float(s_per_hour)) + float(bonus))
    except ValueError:
        print('Введите три параметра')

s_calc()
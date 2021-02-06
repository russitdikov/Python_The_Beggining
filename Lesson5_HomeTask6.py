# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

user_input = input('введите числа через пробел ')
sum_of_f = 0
with open('f_hometask5.txt', 'w+', encoding='utf-8')as write_file:
    write_file.writelines(user_input)
    write_file.seek(0)
    list_from_file = write_file.read().split()
for el in list_from_file:
    try:
        sum_of_f += float(el)
    except ValueError:
        print('число введено не корректно ')

print(sum_of_f)

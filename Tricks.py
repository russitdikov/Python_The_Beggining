#Объединение списков с помощью sum
my_list = [[10, 20, 30], [40, 50], [60], [70, 80, 90]]
print(sum(my_list, []))
# поиск уникальных значений. Преобразование списка во множество
my_list = [10, 10, 3, 4, 5, 9, 30, 30]
print(list(set(my_list)))
# обмен значениями через кортеж
var_1, var_2 = 20, 30
print(var_1, var_2)
var_1, var_2 = var_2, var_1
print(var_1, var_2)
# Вывод значений не существующего ключа
my_dict = {'k_1': 20, 'k_2': True, 'k_3': 'text'}
print(my_dict.get('k_4'))
# поиск наиболее часто встречающегося элемента списка
my_list = [10, 20, 20, 20, 30, 50, 70, 30]
print(max(set(my_list), key=my_list.count))
# распаковка последовательности
my_list = [20, 30, 40, 50]
*el_1, el_2, el_3 = my_list
print(el_1, el_2, el_3)
el_1, *el_2, el_3 = my_list
print(el_1, el_2, el_3)
el_1, el_2, *el_3 = my_list
print(el_1, el_2, el_3)
el_1, el_2, el_3, *el_4 = my_list
print(el_1, el_2, el_3, el_4)
el_1, el_2, el_3, el_4, *el_5 = my_list
print(el_1, el_2, el_3, el_4, el_5)
# Вывод без перевода строки
for el in ["ab", "ra", "kada", "bra"]:
    print(el, end='')
# Сортировка словаря по значениям
my_dict = {'python': 1991, 'java': 1995, 'c++': 1983}
print(sorted(my_dict, key=my_dict.get))
# Нумерованные списки
for ind, el in enumerate(['ноль', 'один', 'два', 'три']):
    print(ind, el)
# Транспонирование(замена строк и столбцов)матрицы
old_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
new_list = zip(*old_list)
print(list(new_list))




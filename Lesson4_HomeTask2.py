# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше
# предыдущего элемента.Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор. Пример исходного списка:
# [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].Результат: [12, 44, 4, 10, 78, 123].

initial_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [el for el in initial_list if
            initial_list.index(el) != 0 and initial_list[initial_list.index(el)] > initial_list[
                initial_list.index(el) - 1]]

print(new_list)

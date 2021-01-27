# 4.	Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

raiting_list = [7, 6, 3, 2, 2, 2]
user_digit = int(input('Введите число: '))
if user_digit not in raiting_list:
    if user_digit < raiting_list[0]:
        raiting_list.append(user_digit)
    else:
        raiting_list.insert(0, user_digit)
else:
    index_of_same = raiting_list.index(user_digit)
    num_of_same = raiting_list.count(user_digit)
    raiting_list.insert(index_of_same + num_of_same, user_digit)
print(raiting_list)

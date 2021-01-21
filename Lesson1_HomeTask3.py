# 3.	Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_number = int(input('Введите число: '))

print(int(f'{user_number}') + int(f'{user_number}{user_number}') + int(f'{user_number}{user_number}{user_number}'))

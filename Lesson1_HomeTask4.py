# 4.	Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_number = int(input('введите целое положительное число: '))

max_num = 0

while user_number // 10 != 0:
    test_number = user_number % 10
    user_number = user_number // 10
    if max_num < test_number:
        max_num = test_number

print(max_num)

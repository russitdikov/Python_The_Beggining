# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его
# работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyOwnExeption(Exception):
    def __init__(self, text):
        self.text = text


digit_1 = input('Введите числитель: ')
digit_2 = input('Введите знаменатель: ')

try:
    if int(digit_2) == 0:
        raise MyOwnExeption('Ай-ай-ай. На ноль делить нельзя')
    int(digit_1) / int(digit_2)
except (ValueError, MyOwnExeption) as err:
    print(err)
else:
    print(int(digit_1) / int(digit_2))

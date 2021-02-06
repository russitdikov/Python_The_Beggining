# 1.	Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.

name = input('Как Вас зовут?')
age = int(input('сколько Вам лет?'))

time = input('Который сейчас час?')

print('Значит Вас зовут', name, '.Вам', age, 'лет', ', и сейчас', time)
print(f'Значит Вас зовут {name}.Вам {age} лет и сейчас уже {time}')

right_answer = [4, 'замок']

print('проверим Ваш интеллект')

question_1 = None

while True:
    question_1 = int(input('Сколько будет два умножить на два?'))
    if question_1 == right_answer[0]:
        print('Верно. Следующий вопрос')
        break
    else:
        print('А вы точно не соврали насчет возраста? попробуйте еще раз')

question_2 = None

while question_2 != right_answer[1]:
    question_2 = input('Отгадайте загадку: не лает не кусает, а в дом не пускает.')
    if question_2 == right_answer[1]:
        print('Верно. Ай Вы молодец!')
    else:
        print('Не верно. Соберитесь.')

after_column = 3.195

print(type(after_column), after_column)
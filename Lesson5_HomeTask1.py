# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

while True:
    user_input = input('введите текст ')
    with open('text_l5_ht1.txt', 'a', encoding='utf-8') as first_file:
        first_file.writelines(f'{user_input}\n')
    if user_input == '':
        break








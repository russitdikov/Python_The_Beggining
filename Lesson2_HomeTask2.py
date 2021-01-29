# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

user_list = []

list_index = int(input('введите количество элементов списка: '))

while list_index != 0:
    list_el = input('Введите элемент списка: ')
    user_list.append(list_el)
    list_index -= 1

even_list = user_list[1::2]
odd_list = user_list[::2]
print('user_list', user_list)
new_list = []
user_list_lengh = len(user_list)
odd_list_lengh = len(odd_list)

if user_list_lengh <=1:
    print('С введенными данными операция не возможна')
    new_list = user_list
else:
    for i in range(0,odd_list_lengh):
        if len(even_list) > i:
            new_list.append(even_list[i])
            new_list.append(odd_list[i])
        else:
            new_list.append(odd_list[i])
print(new_list)


# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    """возвращает сумму наибольших двух аргументов"""
    list_var = [a, b, c]
    max_v = max(list_var)
    list_var.remove(max_v)
    max_v_2 = max(list_var)
    return max_v + max_v_2


print(my_func(float(input('А: ')), float(input('B: ')), float(input('C: '))))

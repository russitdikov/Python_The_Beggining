# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
# матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, list_of_the_lists):
        self.list_of_the_lists = list_of_the_lists

    def __str__(self):
        self.output = [i for i in self.list_of_the_lists]
        for el in self.output:
            for i in el:
                print(i, end=' ')
            print()

    def __add__(self, input_matrix):
        self.input_matrix = input_matrix
        if len(input_matrix) != len(self.list_of_the_lists):
            print('операция работает только с равнозначными матрицами')
        elif len(input_matrix[0]) != len(self.list_of_the_lists[0]):
            print('операция работает только с равнозначными матрицами')
        else:
            for i in range(len(input_matrix)):
                for k in range(len(input_matrix[i])):
                    print((input_matrix[i][k] + self.list_of_the_lists[i][k]), end=' ')
                print('')
        return ('')


in_matrix_1 = Matrix([[1, 2, 3], [10, 10, 10]])
in_matrix_2 = Matrix([[10, 10, 10], [1, 2, 3]])

# in_matrix_1.__str__()
# in_matrix_2.__str__()

print(in_matrix_1.__add__([[10, 10, 10], [1, 2, 3]]))

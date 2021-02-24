# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
# перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры
# класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность
# полученного результата.

class My_Complexdigit:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return f'({self.x + other.x}+{(self.y + other.y)}j)'

    def __mul__(self, other):
        return f'({(self.x * other.x) - (self.y * other.y)}+{(self.x * other.x) + (self.y * other.y)}j)'

#для проверки
x = My_Complexdigit(5, 6)
y = My_Complexdigit(10, 10)

z = 5 + 6j
w = 10 + 10j

print(x * y)

print(z * w)

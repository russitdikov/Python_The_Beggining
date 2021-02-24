# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся
# пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clouth(ABC):
    total_spending = 0

    def __init__(self, name, input_par):
        self.name = name
        self.input_par = input_par

    def __add__(self, other):
        Clouth.total_spending += round((self.spending + other.spending), 2)
        return Suit(self.name, 0)

    def __str__(self):
        return f'{Clouth.total_spending}'


class Coat(Clouth):

    @property
    def spending(self):
        return self.input_par / 6.5 + 0.5


class Suit(Clouth):

    @property
    def spending(self):
        return (2 * self.input_par + 0.3) / 100


coat1 = Coat('Coat1', 43)
suit1 = Suit('Suit 1', 172)
coat2 = Coat('Coat2', 40)

print(round((2 * 172 + 0.3) / 100 + (43 / 6.5 + 0.5) + (40 / 6.5 + 0.5), 2))

print(coat1 + suit1 + coat2)

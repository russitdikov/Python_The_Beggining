# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
# метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого
# из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
# описанный метод для каждого экземпляра.

class Stationery:
    title = 'Канцтовары'

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки ')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки. {self.title} пишет текст')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки. {self.title} рисует наброски')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки. {self.title} выделяет ключевой текст')


pen_1 = Pen('Ручка')
pencil_1 = Pencil('Карандаш')
handle_1 = Handle('Маркер')
print(Stationery.title)
print(Pen.title)
print(pen_1.title)
pen_1.draw()
pencil_1.draw()
handle_1.draw()

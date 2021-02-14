# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running
# (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый)
# — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный
# метод.Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.

import time
import turtle

turtle.speed(200)


def circle_fill(x, y):
    turtle.pencolor('white')
    turtle.setpos(x, y)
    turtle.begin_fill()
    turtle.color('black')
    turtle.circle(20)
    turtle.end_fill()


def light_switch(intit_y, end_y, color, sleep_time):
    turtle.pencolor('white')
    turtle.setpos(71, intit_y)  # 25
    turtle.setpos(71, end_y)  # 145
    turtle.setpos(50, end_y)
    turtle.begin_fill()
    turtle.color(color)  # 'red'
    turtle.circle(20)
    turtle.end_fill()
    time.sleep(sleep_time)
    turtle.begin_fill()
    turtle.color('black')
    turtle.circle(20)
    turtle.end_fill()


for i in range(2):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)

circle_fill(50, 145)
circle_fill(50, 85)
circle_fill(50, 25)


class TrafficLight:
    def __init__(self):
        self.__color = 'Красный'

    # def SetColor(lcolor):
    #     self.__color = lcolor
    def running(self, repeat_time):
        for i in range(repeat_time):
            light_switch(25, 145, 'red', 7)
            light_switch(145, 85, 'yellow', 2)
            light_switch(85, 25, 'green', 7)


Light1 = TrafficLight()
Light1.running(1)

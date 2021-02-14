# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print('автомобиль поехал')

    def stop(self):
        print('автомобиль остановился')

    def turn(self, direction):
        if direction == 'Left':
            print('автомобиль повернул налево')
        elif direction == 'Right':
            print('автомобиль повернул налево')
        else:
            print('введите направление в формате Right или Left')

    def show_speed(self):
        print(f'Ваша скорость {self.speed}')


class TownCar(Car):
       def show_speed(self):
        if self.speed > 60:
            print(f'Превышение!!! Ваша скорость {self.speed}')
        else:
            print(f'Ваша скорость {self.speed}')


class WorkCar(Car):
       def show_speed(self):
        if self.speed > 40:
            print(f'Превышение!!! Ваша скорость {self.speed}')
        else:
            print(f'Ваша скорость {self.speed}')


class SportCar(Car):
    pass



class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed,color,name)
        self.is_police = False


police_car1 = PoliceCar(100, 'red', 'cop1')
town_car1 = TownCar(100, 'green', 'tc1')
town_car2 = TownCar(50, 'black', 'tc2')
work_car1 = WorkCar(100, 'blue', 'wc1')
sport_car1 = SportCar(100, 'yellow', 'sc1')

police_car1.go()
police_car1.turn('Let')
police_car1.turn('Left')
police_car1.stop()
print(police_car1.__dir__())

town_car1.show_speed()
print(town_car1.color)
town_car2.show_speed()

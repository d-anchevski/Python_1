"""
Задание 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).

А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


# Class block
import random


class Car:
    car_lst = []  # A list of all class instances

    def __init__(self, speed=100, color="white", name="NoName"):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
        Car.car_lst.append(self)

    def go(self):
        print(f"The car has started")

    def stop(self):
        print(f"The car has stopped")

    def turn(self, direction="Right"):
        print(f"The car has turned {direction}")

    def show_speed(self):
        print(f"The car's speed is {self.speed} km/h")
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if super(TownCar, self).show_speed() > 60:
            print(f"The speed is by {self.speed-60} km/h exceeded")


class SportCar(Car):  # No task, no solution :)
    pass


class WorkCar(Car):
    def show_speed(self):
        if super(WorkCar, self).show_speed() > 40:
            print(f"The speed is by {self.speed - 40} km/h exceeded")


class PoliceCar(Car):

    def __init__(self, speed=100, color="white", name="NoName"):
        super().__init__(speed, color, name)
        self.is_police = True


# Client code
c = Car()
tc1 = TownCar(55, "Black", "Zepr")
tc2 = TownCar(65, "Green", "Zepr2")
sc = SportCar(150, "Red", "F1")
wc = WorkCar(41, "Black", "Vehicle")
pc = PoliceCar(90, "White'n'Blue", "Chrysler")

for el in Car.car_lst:
    print(f"\nCar {el.name} is {el.color} and has the speed {el.speed} km/h")
    el.go()
    el.show_speed()
    el.turn(random.choice(["Left", "Right", "Back", "Around"]))
    el.stop()
    print(f"Is police = {el.is_police}")

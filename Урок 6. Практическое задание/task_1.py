"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
# Import block
import time


# Classes block

class TrafficLight:

    def __init__(self, name, green_dur):
        try:
            green_dur_int = int(green_dur)
        except ValueError:
            return
        self.name = name
        self.color_set = {"Red": 7, "Yellow": 2, "Green": green_dur_int}
        self.__color = "Off"

    def running(self):
        for el in self.color_set.items():
            self.__color = el[0]
            print(f'\r{self.__color} light is glowing.')
            for i in range(el[1], 0, -1):  # Activating a countdown
                print(f"\r{i}", end="")
                time.sleep(1)
        print("\r ")

# End of Classes block


# Client code
nc = 1  # Just a number of planned cycles of traffic lights functioning
tr_l = TrafficLight("Traffic Lights N1", "4")
tr_l1 = TrafficLight("Traffic Lights N2", 1)  # Just another sample of class to check

trl_lst = [tr_l, tr_l1]

for el in trl_lst:
    print(f"Traffic lights \"{el.name}\" is functioning")
    for i in range(0, nc):
        el.running()

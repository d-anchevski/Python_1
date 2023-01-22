"""
Задание 2.

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""
# Class block
class Road:
    road_lst = []  # A list of all class instances

    def __str__(self):  # Reloading the inbuilt function to show names of all created Road instances
        return f"Road {self.name}"

    def __del__(self):  # Reloading the inbuilt function by deleting an instance from the instance list
        print(f"\n{self} is deleted")
        Road.road_lst.remove(self)
        print(f"Available Road instances now are:")
        for inst in Road.road_lst:
            print(inst)

    def __init__(self, name, length, width, weight=25, thick=0.05):
        self.name = name
        self._length = length
        self._width = width
        self.weight = weight
        self.thick = thick
        Road.road_lst.append(self)
        return

    def asf_mass_calc(self):
        return self._length * self._width * self.weight * self.thick


# Clint code
road_1 = Road("E95", 3000, 12, 30, 0.1)
road_2 = Road("M1", 5000, 18, thick=0.2)
road_3 = Road("H6321", 1000, 6, weight=20)

for el in Road.road_lst:
    print(f"The total asphalt weight for road {el.name} is {el.asf_mass_calc()} kg")

print("\nAvailable Road instances:")
for el in Road.road_lst:
    print(el)

print(f"\nTrying to delete {road_2}:")
del road_2
# I have no idea why that's not working...
# Especially when it works right during automatic deleting at the end!!!
# Especially because instance road_2 "is not defined" after the delete procedure!!!
# NEED EXPLANATION!!! PLEASE :)
print("End of the attempt")

"""
Задание 5.

Реализовать класс Stationery (канцелярская принадлежность).

Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”

Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).

В каждом из классов реализовать переопределение метода draw.

Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    stat_list = []

    def __init__(self, title):
        self.title = title
        Stationery.stat_list.append(self)

    def draw(self):
        print(f"\nDrawing launched")

    def __str__(self):
        return f"{self.title}"


class Pen(Stationery):
    def draw(self):
        super().draw()
        print(f"Pen \"{self.title}\" is in action")


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print(f"Pencil \"{self.title}\" is in action")


class Handle(Stationery):
    def draw(self):
        super().draw()
        print(f"Handle \"{self.title}\" is in action")


# Client code
pn = Pen("Signer")
pncl = Pencil("Sketcher")
hndl = Handle("Marker")

for inst in Stationery.stat_list:
    inst.draw()

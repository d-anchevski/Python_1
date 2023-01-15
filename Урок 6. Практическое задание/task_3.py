"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
__str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""


# Class block
class Worker:

    def __init__(self, name="Undefined", surname="Undefined", position="Unset", wage=0, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    pos_lst = []  # A list of all class instances

    def __init__(self, name="Undefined", surname="Undefined", position="Unset", wage=0, bonus=0):
        super().__init__(name, surname, position, wage, bonus)
        Position.pos_lst.append(self)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")

    def __str__(self):
        return f"The employee {self.get_full_name()} has the total income of {self.get_total_income()}"


# Client code

ps_adp = Position("Dmitri", "Anchevski", "CPI", 3000, 500)
ps_aiv = Position("Inesse", "Anchevskaya", "I1K", 2000)


for el in Position.pos_lst:
    print(f"\nThe employee's N{Position.pos_lst.index(el)+1} full name is {el.get_full_name()}")
    print(f"Total income of the employee is {el.get_total_income()}")
    print(f"Str testing: {el}")
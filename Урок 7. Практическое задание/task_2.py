"""
Задание 2.

Реализовать проект расчета суммарного расхода ткани на производство одежды.

Единственный класс этого проекта — одежда (класс Clothes).

К типам одежды в этом проекте относятся пальто и костюм.

У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property

Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57

Два класса: абстрактный и Clothes
"""


# Class block
from abc import ABC, abstractmethod


class AbstractClothes(ABC):

    @abstractmethod
    def fabric_calc(self):
        pass


class Clothes(AbstractClothes):
    cl_types = {"Coat": "Size", "Costume": "Height"}  # Dictionary of clothes types and their calculation parameters
    cl_to_sew_lst = []  # A list of all clothes items created

    @staticmethod
    def total_calc():
        total_fabric = 0
        for el in Clothes.cl_to_sew_lst:
            total_fabric += el.fabric_needed
        print(f"Total fabric: {total_fabric:.2f} ")

    def __init__(self, cl_type, value):
        self.cl_type = cl_type  # Type of the clothes item
        self.value = value  # The value of parameter for fabric calculation
        self.val_type = Clothes.cl_types.get(cl_type)  # The type of calculation parameter
        if self.val_type is None:  # Checking for unknown Clothes types
            print(f"Order creation is cancelled! Type '{cl_type}' of clothes is unknown!")
            return None
        Clothes.cl_to_sew_lst.append(self)  # Adding to a overall list
        self.fabric_needed = self.fabric_calc  # Calculating the needed fabric amount for the item being created

    def __str__(self):
        return f"Item N{Clothes.cl_to_sew_lst.index(self)} - {self.cl_type} - {self.val_type} {self.value} - " \
               f"fabric: {self.fabric_needed:.2f}"

    @property
    def fabric_calc(self):
        sub_res = 0
        if self.cl_type == "Coat":
            sub_res = self.value / 6.5 + 0.5
        elif self.cl_type == "Costume":
            sub_res = self.value * 2 * 0.3
        else:
            print(f"Calculation of the instance with type {self.cl_type} aborted! Unknown type of clothes!")
            sub_res = None
        return sub_res


# Client code
Clothes("Coat", 160)
Clothes("Costume", 50)
Clothes("Coat", 140)
Clothes("Costume", 25)
Clothes("Coatillio", 100)
Clothes("Costumillio", 10)

for el in Clothes.cl_to_sew_lst:
    print(el)
Clothes.total_calc()

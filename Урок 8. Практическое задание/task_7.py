"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


# Class block
class Complex:

    def __init__(self, real, image):
        self.real = real
        self.image = image

    def __add__(self, other):
        real = self.real + other.real
        image = self.image + other.image
        return Complex(real, image)

    def __mul__(self, other):
        """ (a1+ib1) * (a2+ib2) = a1a2+ia1b2 + ib1a2 - b1b2 = (a1a2-b1b2) + i(a1b2+b1a2)"""
        real = self.real * other.real - self.image * other.image
        image = self.real * other.image + self.image * other.real
        return Complex(real, image)

    def __str__(self):
        return f"({self.real}+{self.image}i)"


# Client block

v1 = Complex(2, 3)
v2 = Complex(4, 5)

print(f"({v1.real}+{v1.image}i) + ({v2.real}+{v2.image}i) = {v1 + v2}")
print(f"({v1.real}+{v1.image}i) * ({v2.real}+{v2.image}i) = {v1 * v2}")


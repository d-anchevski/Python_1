"""
Задание 1.

Реализовать класс «Дата», на уровне класса определить атрибут day_month_year,
присвоить ему значение

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц,
год, преобразовывать их тип к типу «Число» и делать атрибутами класса.

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


# Import block
from datetime import date


# Class block
class Data:
    day_month_year = 0

    @staticmethod
    def dmy_validator(date_input: f"00-00-0000"):
        split = date_input.split('-')
        for i in range(0, 3):
            try:
                split[i] = int(split[i])
            except ValueError:
                print(f"Value error in {'Day' if i==0 else 'Month' if i==1 else 'Year'} value: '{split[i]}'")
                return None
        if split[0] > 31 or split[1] > 12:
            print(f"Not the date format")
            return None
        return split

    @classmethod
    def dmy_extractor(cls, dmy_inp):
        dmy = Data.dmy_validator(dmy_inp)
        if not dmy:
            return
        print(f"{[t for t in dmy]}")
        Data.day_month_year = date(dmy[2], dmy[1], dmy[0])


# Client code
test_lst = ["12-01-2022", "24-16-2003", "32-11-2021",
            "02-11-2ooo", "o1-12-1984", "23-1o-2003"]

for el in test_lst:
    Data.dmy_extractor(el)
print(Data.day_month_year)

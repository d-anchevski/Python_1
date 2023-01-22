"""
Задание 1. Создать список и заполнить его элементами различных типов данных.
Реализовать проверку типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.

Пример:
для списка [5, "string", 0.15, True, None]
результат

<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
"""
from datetime import datetime

worker_1 = ["Dmitrij", 36, 2560.5, True, None, ["Project_1", "Project_4"], ("N23-42RN", datetime(1986, 6, 27), "Minsk")]

# DType check cycle:
for el in worker_1:
    print(type(el))

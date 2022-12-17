"""
Задание 2. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3

Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""

# N1 Creating a str-type variable
var_str = input("Enter integer numbers, separated by spaces\n")

# N2 Creating a list from the digits of the created variable
var_lst = var_str.split(" ")
print(f"This is the list gotten from your digits : {var_lst}")

# N3 Calculating an operator to control cycle condition
op_1 = len(var_lst) % 2

# N4 Creating a bubble-type sorting (with double step and operation control)
for i in range(0, len(var_lst) - 1 - op_1, 2):
    var_x = var_lst[i + 1]
    var_lst[i + 1] = var_lst[i]
    var_lst[i] = var_x

print(f"This is the moved list: {var_lst}")

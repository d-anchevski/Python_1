"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""


def my_funct(x, y):
    # Block#1 Value check
    if x <= 0 or (y > 0):
        return

    # Block#2 Calculations [z = x ^ y --> z = 1 / x ^ (-y)]
    z = 1  # Initial value
    for i in range(1, -y + 1):
        z = z / x
    return z


# Main
test_lst = [[10, -2], [8.5, -3], [16.25, -2], [2, -2]]  # List of test values

# Solution for all the pairs in the list
for itm in test_lst:
    print(f"{itm[0]} ^ ({itm[1]}) = {my_funct(itm[0], itm[1])}")

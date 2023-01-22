"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroDivExc(Exception):
    def __init__(self):
        print("Division by zero is prohibited! Reenter your data!")


# Client code
def user_input():
    a = input(f"Enter the divisible:")
    b = input(f"Enter the divider: ")
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print(f"You've entered a non-numeric value! Reenter you data")
        return None
    return [a, b]


lst = []

while True:
    lst = user_input()
    if not lst:
        continue
    try:
        if lst[1] == 0:
            raise ZeroDivExc()
    except ZeroDivExc as zde:
        continue
    break

print(f"{lst[0]} / {lst[1]} = {lst[0] / lst[1]}")



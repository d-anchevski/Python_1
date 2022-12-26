"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""


def div_2(dvs: float, dvd: float):
    if float(dvd) == 0:  # converting to float in case a user enters str values
        return "Error! Division on zero is forbidden!"
    return str(float(dvs) / float(dvd))  # converting to float in case a user enters str values


while True:  # Multitime input test module
    divisible = input("Enter a divisible or 'q' to terminate: ")
    if divisible == "q":
        break

    # Converting to float (after input value check)
    divisible = float(divisible)
    divider = float(input("Enter a divider: "))

    # Getting an answer from the function
    answer = div_2(divisible, divider)

    # Formatting the answer according to its value
    result = answer if answer[0:5] == "Error" else answer[0:(answer.index('.') + 3)]

    # Printing results
    print(f"The result from division of {divisible} on {divider} is {result}")

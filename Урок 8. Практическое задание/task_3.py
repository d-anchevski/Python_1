"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""
import string


class OnlyNumeric(Exception):
    def __init__(self, non_num):
        print(f"'{non_num}' is not a numeric and cannot by added to the list!")


# Client code
lst = []
while True:
    comma_ctrl = 0
    val = input("Enter the next value or press just enter to break: ")
    if val == "":
        break
    val = val.replace(",", ".")  # Supposing "," can also be a separator
    try:
        for dig in val:
            if dig == ".":
                if comma_ctrl > 0:  # Comma can be only unique in the
                    raise OnlyNumeric(val)
                comma_ctrl += 1
                continue
            elif dig not in string.digits:
                raise OnlyNumeric(val)
        lst.append(float(val))
    except OnlyNumeric as only_num:
        only_num

    print(f"The actual list is: {lst}\n")

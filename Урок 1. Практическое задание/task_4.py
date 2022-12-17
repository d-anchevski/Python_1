"""
Задание 4.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.

Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""

value_str = input("Enter a natural number:\n")

# Вариант с использованием цикла for и enumerate
dgt_max = 0
for i, digit in enumerate(value_str):
    if int(value_str[i]) > dgt_max:
        dgt_max = int(digit)

print(f"WITH FOR AND ENUMERATE: The highest digit in the input number: {dgt_max}")

# Но можно реализовать и с помощью WHILE и длины строки

dgt_max = 0
i = 0
while i < len(value_str):
    if int(value_str[i]) > dgt_max:
        dgt_max = int(value_str[i])
    i += 1
print(f"WITH WHILE AND LEN: The highest digit in the input number: {dgt_max}")

"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

num_str = input("Enter a natural number: \n")
num_str2 = num_str * 2
num_str3 = num_str * 3

result=int(num_str)+int(num_str2)+int(num_str3)
print(f"Solution: {num_str} + {num_str2} + {num_str3} = {result}")

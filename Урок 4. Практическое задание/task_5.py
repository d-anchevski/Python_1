"""
5. Реализовать формирование списка, используя функцию range()
и возможности генераторного выражения.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать лямбда-функцию и функцию reduce().
"""
from functools import reduce

result1 = reduce(lambda x, y: x * y, (el for el in range(100, 1001) if el % 2 == 0))  # For a "random" list of values
print(f"Result with even-check: {result1}")

# But for a given list we can just take every second element - and it will be even

result2 = reduce(lambda x, y: x * y, (el for el in range(100, 1001, 2)))  # For a directly given list
print(f"Result with every second element: {result2}")

# An ordinary calculation - just to check
result3 = 1
for el in range(100, 1001, 2):
    result3 = result3 * el
print(f"Traditional way result: {result3}")

print(f"\nAll the results are {'equal' if result1 == result2 and result1 == result3 else 'not equal'}")

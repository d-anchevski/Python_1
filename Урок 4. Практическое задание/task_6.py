"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
"""

# Test values block
from itertools import count, cycle
initializer = 14

# Preparation block
control_a = 20
control_b = 40
res_a_lst = []
res_b_lst = []

# Solution block
# Task A
for i in count(initializer):
    res_a_lst.append(i)
    if i >= control_a:
        break
print(f"Here are the 'count'-values: {res_a_lst}")

# Task B (will use res_lst as and iterable array)
i = 1  # just a controlling iterator
for el in cycle(res_a_lst):
    res_b_lst.append(el)
    i += 1
    if i > control_b:
        break
print(f"Here are the 'cycled'-values: {res_b_lst}")
print(f"There are {len(res_b_lst)} elements in the cycled array. And the limit was {control_b}")
print(f"Everything is {'ok' if len(res_b_lst) == control_b else 'wrong'}")


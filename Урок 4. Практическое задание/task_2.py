"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""

# Traditional way:
init_lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

proc_lst = []
for i in range(1, len(init_lst)):
    if init_lst[i] > init_lst[i - 1]:
        proc_lst.append(init_lst[i])
print(f"This is made traditionally: {proc_lst}")

# LS-expression (generator expression) way:
proc_lst = (init_lst[i] for i in range(1, len(init_lst)) if init_lst[i] > init_lst[i - 1])
print(f"This is made by LC-expression: {list(proc_lst)}")  # Wrapping into list to see the contents of generator

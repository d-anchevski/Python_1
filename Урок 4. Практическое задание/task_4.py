"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генераторное выржаение.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

init_lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

proc_lst = (init_lst[i] for i in range(0, len(init_lst)) if init_lst[i] not in
            (init_lst[j] for j in range(i + 1, len(init_lst))) and init_lst[i] not in (init_lst[k] for k in
                                                                                       range(0, i)))
# I believe this could have benn resolved easier - but though here I did use even three generator-expressions,
# two of which are even in-built )))

print(f"The resulting array is: {list(proc_lst)}")

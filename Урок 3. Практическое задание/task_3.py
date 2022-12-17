"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func_sort(arg1, arg2, arg3):
    """ Sorts the list of gotten values and returns the two least of them"""
    mfs_list = [float(arg1), float(arg2), float(arg3)]
    mfs_list = sorted(mfs_list)
    return mfs_list[0:2]


def my_func_nonsort(arg1, arg2, arg3):
    """Finds two least values from the list and returns them"""
    mfs_list = [float(arg1), float(arg2), float(arg3)]
    min_1 = min(mfs_list)
    mfs_list.remove(min_1)
    min_2 = min(mfs_list)
    return min_1, min_2


# Main
test_arg1 = 43.2
test_arg2 = 14.6
test_arg3 = 1.45

result_lst = my_func_sort(test_arg1, test_arg2, test_arg3)
print(f"SORTED: The smallest values from {test_arg1},{test_arg2} and {test_arg3} are: {result_lst}")

res1, res2 = my_func_nonsort(test_arg1, test_arg2, test_arg3)
print(f"UNSORTED: The smallest values from {test_arg1},{test_arg2} and {test_arg3} are: {result_lst}")

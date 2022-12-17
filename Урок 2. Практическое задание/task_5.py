"""
5. Реализовать структуру «Рейтинг», представляющую собой не
возрастающий набор натуральных чисел
(каждый элемент ряда меньше или равен предыдущему).

У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2].
"""

# N1: Initial list setting:
rating_lst = [6, 5, 4, 3, 2, 2]

# N2: Endless cycle of data entering (terminates on break)
while True:
    print(f"Current rating-list: {rating_lst}")
    val_str = input("Enter a natural number or press 'Enter' to abort the program: ")
    if val_str == "": # Termination condition
        break
    else:
        val_int = int(val_str) # Trasforming string into integer

    for i, el in enumerate(rating_lst): # cycling all the list-elements
        if val_int >= el:
            rating_lst.insert(i, val_int) #inserting a number
            break
    if val_int < rating_lst[-1]:
        print(F"Rating last is: {rating_lst[-1]}")
        rating_lst.append(val_int)

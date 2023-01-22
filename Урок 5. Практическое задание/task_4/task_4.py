"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""


def wrong_data_to_none(pos):
    """Appends a piece of wrong data to the special array and converts the wrong salary value into None"""
    error_lst.append([pos, el[0]])  # dealing with outer scope variables
    emp_sal_lst[pos][1] = None  # dealing with outer scope variables


# Variables determination
emp_sal_lst = []

# Opening the test file
read_file = open("Test_File_N4.txt", "r")

# Extracting data line by line
data_lst = read_file.readlines()

# Splitting lines by values
for el in data_lst:
    emp_sal_lst.append(el.split(' '))
print(f"Unconverted data list {emp_sal_lst}")

# Converting string numbers into float-type
error_lst = []
for i, el in enumerate(emp_sal_lst):
    try:
        el[1] = float(el[1])
        if el[1] < 0:
            wrong_data_to_none(i)
    except ValueError:
        wrong_data_to_none(i)
        continue
if error_lst:
    print("\nThe salary values in the initial file were wrong for the next employees:")
    for el in error_lst:
        print(el[1])
    print("Their data excluded from the list")
    print(f"Remaining data:\n {emp_sal_lst}")

# Finding employees earning less than 20k
none_ctrl = 0
print("\nEmployees with salary less than 20k:")
for el in emp_sal_lst:
    if el[1] is None:
        continue
    elif el[1] < 20000:
        print(f"{el[0]} - {el[1]}")
        none_ctrl += 1
if none_ctrl == 0:
    print("None")

# Calculating the average salary
sum_sal = 0
relevant_num = len(emp_sal_lst)
for el in emp_sal_lst:
    if el[1]:
        sum_sal += el[1]
    else:
        relevant_num -= 1
av_sal = sum_sal/relevant_num
print(f"\nThe average salary of employees is: {av_sal}")
if error_lst:
    print("The result is actually not totally relevant due to the stated pieces of incorrect initial data")
read_file.close()
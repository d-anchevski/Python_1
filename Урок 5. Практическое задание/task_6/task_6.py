"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

# Assuming that data format in the file is exactly as in the example above:
# - ":" after subject's name
# - three spaces between values
# - long dash for absent values
# - lesson types in brackets right after the number of hours (without a space)

# Special symbols block
sp = "   "

# Variables' preparation block
result_dict = {}

# Opening the file
read_fl = open("Test_file_N6.txt", "r")

# Extracting its data, splitting by values, reducing unnecessary symbols
data_lst = read_fl.readlines()
for i, el in enumerate(data_lst):
    data_lst[i] = el.split(sp)
    for j, el1 in enumerate(data_lst[i]):
        data_lst[i][j] = data_lst[i][j][0:data_lst[i][j].find('(')]
# In the given situation the returned '-1' value in case of no '(' to be found will du us a favour by
# - reducing unnecessary ':' from the subject's name
# - reducing fields with "—" to an empty field"""
# converting string type numbers into float
        try:
            data_lst[i][j] = float(data_lst[i][j])
        except ValueError:
            continue
    sum_hours = sum([el for el in data_lst[i] if type(el) is float])
    result_dict.update({data_lst[i][0]: sum_hours})
print(result_dict)
read_fl.close()

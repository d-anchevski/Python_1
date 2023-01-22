"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные
о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

# Preparation block
import json
profits = []
not_negative_num = 0
profit_dict = {}
av_profit_dict = {}
total_lst = []

# Opening the file
read_fl = open("Test_file_N7.txt", "r")

# Extracting its data, splitting by values, calculating incomes, creating resulting list
data_lst = read_fl.readlines()
for i, el in enumerate(data_lst):
    data_lst[i] = el.split(' ')
    for j, el1 in enumerate(data_lst[i]):
        try:
            data_lst[i][j] = float(data_lst[i][j])
        except ValueError:
            continue
    profit = data_lst[i][2] - data_lst[i][3]  # Revenue - loses
    profits.append(profit)
    not_negative_num = len([el for el in profits if el >= 0])
    profit_dict.update({data_lst[i][0]: profit})
av_profit = sum([el for el in profits if el >= 0]) / not_negative_num
av_profit_dict = {'average_profit': av_profit}
total_lst.extend([profit_dict, av_profit_dict])
print(f"Incomes of companies are:\n {profits}\n Average income of companies with not negative saldo "
      f"(there are {not_negative_num} of them) is: {av_profit}")
print(f"\nThe resulting list: {total_lst}")

with open("Test_file_N7.2.json", "w+") as write_file:
    json.dump(total_lst, write_file, ensure_ascii=False)

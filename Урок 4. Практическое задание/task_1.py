"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

source_name, stake_inp, hours_inp, bonus_inp = argv
error_ans = "'Error! Perhaps, you've entered a wrong value'"


def salary_calc(stake_s, hours_s, bonus_s):
    ''' Calculates the amount to be paid, basing on input Data'''
    try:
        stake = float(stake_s)
        hours = float(hours_s)
        bonus = float(bonus_s) if bonus_s != "" else 0
    except ValueError:
        return
    if hours < 0 or stake < 0:
        return
    return stake * hours + bonus


result = salary_calc(stake_inp, hours_inp, bonus_inp)
print(f"Amount to pay is {result if result else error_ans}\nDecided by {source_name} :)")


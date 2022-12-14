"""
Задание 6.

Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня,
на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b
 и выводить одно натуральное число — номер дня.

Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""

dist_1 = float(input("Enter the first day result:\n"))
dist_goal = float(input("Enter the goal distance:\n"))
dist_imp_prc = float(input("Enter daily improvement in percents:\n")) / 100  # чтобы не совсем хардкод

dist_imp = 0.1  # хардкод, чтобы точно соответствовать задаче

dist_act = dist_1
count_days = 1
print(f"{count_days} day: {dist_act:.2f}")
while dist_act < dist_goal:
    dist_act += dist_act * dist_imp
    print(f"{count_days} day: {dist_act:.2f}")
    count_days += 1

if count_days > 1:  # На случай, если достижение будет уже в первый день (то есть цикл не запустится ни разу)
    count_days -= 1

print(f"Answer: on the {count_days} day the athlete achieved the result - not less that {dist_goal: .2f} km")

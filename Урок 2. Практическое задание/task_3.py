"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

# N1 Creating list and dict arrays for month classification
month_yeartime_lst_1 = ["Winter", "Winter",
                        "Spring", "Spring", "Spring",
                        "Summer", "Summer", "Summer",
                        "Autumn", "Autumn", "Autumn",
                        "Winter"]

month_yeartime_dict_2 = {1: "Winter", 2: "Winter",
                         3: "Spring", 4: "Spring", 5: "Spring",
                         6: "Summer", 7: "Summer", 8: "Summer",
                         9: "Autumn", 10: "Autumn", 11: "Autumn",
                         12: "Winter"}
# N2: User requst
month_num = int(input("Enter a month number: "))

# N3: Comparing cycle (with initial range check)
if month_num < 1 or month_num > 12:
    print("Number is out of the months' number range. The program terminates")
else:
    print(f"Result by the list: {month_yeartime_lst[month_num - 1]}")
    print(f"Result by the dictionary: {month_yeartime_dict.get(month_num)}")

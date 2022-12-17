"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
# ---------------------------------------------------------
# - Primary idea (not really adequate though working )) ) -
# ---------------------------------------------------------
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
# N2: User request
month_num = int(input("Enter a month number: "))

# N3: Comparing cycle (with initial range check)
if month_num < 1 or month_num > 12:
    print("Number is out of the months' number range. The program terminates")
else:
    print(f"Result by the list: {month_yeartime_lst_1[month_num - 1]}")
    print(f"Result by the dictionary: {month_yeartime_dict_2.get(month_num)}")

# --------------------------
# - More adequate solution -
# --------------------------

# Via Dictionary
yeartime_months_dict = {"Winter": [1, 2, 12], "Spring": [3, 4, 5], "Summer": [6, 7, 8], "Autumn": [9, 10, 11]}
for itm in yeartime_months_dict.items():
    if month_num in itm[1]:
        print(f"Result by the adequate dictionary via cycle: {itm[0]}")

# Via list
yeartime_months_list = [[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
yeartimes = ["Winter", "Spring", "Summer", "Autumn"]
for i, itm in enumerate(yeartime_months_list):
    if month_num in itm:
        print(f"Result by the adequate lists via cycle: {yeartimes[i]}")

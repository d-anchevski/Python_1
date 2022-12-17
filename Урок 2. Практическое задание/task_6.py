"""
6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.

Пример:

{
“названия”: [“компьютер”, “принтер”, “сканер”],
“цены”: [20000, 6000, 2000],
“количества”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

# -------------------------------
# - TASK 1 - Creating a database -
# -------------------------------

# N1 Creating a dictionary structure

"""# Manual categories input (uncomment to check the workability)
categories_str=input("Enter categories names separated via spaces\n")
categories_lst=categories_str.split(" ")"""

# Enforced categories input (just to make testing faster)
categories_lst = ["Title", "Price", "Quantity", "UoM."]

# N2: Endless cycle of filling dictionary with data (terminates on break)
prods = []  # List to fill the products information

# Manual products input (uncomment to check workability)
"""i = 0  # Just and index to print the number of the product being input
while True:
    dict_i = {}
    for el in categories_lst:
        val_str = input(f"Enter the {el} of the product {i+1}: ")
        dict_i.update({el: val_str})
    num_int = int(input("Enter the product's numer: "))
    tuple_i = (num_int, dict_i)
    products.append(tuple_i)
    op_1 = input(f"Enter 'q' and press 'Enter' to terminate: ")
    if op_1 == "q":
        break
    i += 1"""

# Enforced products data input (just to save time)
prods.extend([(101, {'Title': 'Computer', 'Price': '1204', 'Quantity': '12', 'UoM.': 'p.'}),
              (102, {'Title': 'Motherboard', 'Price': '640', 'Quantity': '4', 'UoM.': 'p.'}),
              (103, {'Title': 'Cola', 'Price': '1.4', 'Quantity': '50', 'UoM.': 'gallons'}),
              (104, {'Title': 'OddObject', 'Price': '300', 'Quantity': '2', 'UoM.': 'gallons', 'Rating': '4.5'})]
             )  # in the OddObject there was made and extra category, absent in other items

# Reviewing the created Catalogue:
print("Here is the current catalogue:\n[")
for el in prods:
    print(el)
print("]\n")

# -----------------------------------------------------------------
# - TASK 2 - Analysing the gotten Catalogue according to the task -
# -----------------------------------------------------------------
stats = {}  # the resulting dictionary
cat_set = set()  # For available categories in the dataframe under analysis (using "set" to exclude repeating values)

# Step-by-step solution
# 1. Extracting all unique names of categories in the dataframe
for el in prods:
    for itm in el[1].items():
        cat_set.add(itm[0])

# 2. Filling the categories with available values from the dataframe
for cat in cat_set:
    prod_set = set()  # using temporary set to gather values, renewing for each category
    for el in prods:
        prod_set.add(el[1].get(cat))
    prod_lst = list(prod_set)  # data refactoring from set into list (just to fit the task)
    stats.update({cat: prod_lst})  # Filling the dictionary with pairs "Key-Value"

# Structured output of the dictionary
print("The resulting analytics:\n{")
for itm in stats.items():
    print(f"{itm[0]}: {itm[1]}")
print("}\n")

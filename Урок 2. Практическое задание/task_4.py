"""
4. Пользователь вводит строку из нескольких слов,
разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если слово длинное,
выводить только первые 10 букв в слове.

Пример:
Введите слова через пробел: раз два три
1. раз
2. два
3. три

Введите слова через пробел: раз перерефрижерированность
1. раз
2. перерефриж
"""
# N1: Data input
input_str = input("Enter several words, separated via spaces\n")

# N2: String split and enumerating
list_enum = enumerate(input_str.split(" "))

# N3: Print-cycle with limitation of sting output length
for i, el in list_enum:
    print(f"{i}. {el[:10]}")


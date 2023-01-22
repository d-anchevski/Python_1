"""
Задание 1.

Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.

Пример:
Ведите ваше имя: Василий
Ведите ваш пароль: vas
Введите ваш возраст: 45
Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45
"""
name = input("Enter your name\n")
age_full = int(input("Enter your full age\n"))
height_cm = float(input("Enter your height in cm (with '.'\n"))

print(f"Hello, {name}! You was born {age_full} years ago, and have grown up to {height_cm} cm")

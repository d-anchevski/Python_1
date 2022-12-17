"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

def data_transp(name, surname, birth_year, town, email, phone):
    print(f"{name} {surname}, was born in {birth_year}; Lives in {town}. Contacts: email: {email}, phone: {phone}")


# Main
data_test_1 = ["Dmitri", "Anchevski", "1986", "Minsk", "anchevsky@gmail.com", "+375291234567"]
data_test_2 = ["Someone", "Else", "2010", "Moscow", "no-reply@gmail.com", "+1234567890"]
data_test_3 = ["Mrs", "Smith", "1900", "Town", "e@mail.com", "+9876543210"]

# printing test list, putting variables in different order
data_transp(name=data_test_1[0], surname=data_test_1[1], phone=data_test_1[5], email=data_test_1[4],
            town=data_test_1[3], birth_year=data_test_1[2])
data_transp(phone=data_test_2[5], email=data_test_2[4],
            town=data_test_2[3], birth_year=data_test_2[2], name=data_test_2[0], surname=data_test_2[1])
data_transp(name=data_test_3[0], town=data_test_3[3], birth_year=data_test_3[2], surname=data_test_3[1],
            phone=data_test_3[5], email=data_test_3[4])


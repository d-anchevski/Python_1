"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(word: str):
    str_ttl = str.title(word)
    return str_ttl


def ext_func(l_str: str):
    lstr_lst = l_str.split(' ')
    b_str = ''
    for word in lstr_lst:
        word = int_func(word)
        b_str = b_str+word+' '
    return b_str


# Main
# Test-values
test_list_1 = ['i', 'follow', 'the', 'moskwa', 'down', 'to', 'gorky', 'park']
test_str = "august summer night soldiers will survive listening to the wind of change"

# Solution of task 1
for s in test_list_1:
    print(f"{int_func(s)}")

# Solution of task 2
print(ext_func(test_str))

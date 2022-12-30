"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

# Creating a dictionary
numbers_en_rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

# Opening the test file
read_file = open("Test_File_N3.txt", "r")

# Extracting data line by line
data_lst = read_file.readlines()
print(f"Initially read list: {data_lst}")

# Changing english digits' names into russian ones (using "replace")
for i in range(0, len(data_lst)):
    for tpl in numbers_en_rus_dict.items():
        data_lst[i] = data_lst[i].replace(tpl[0], tpl[1])
read_file.close()
print(f"Translated list: {data_lst}")

# Writing the translated array into a new file
write_file = open("Test_File_N3.2.txt", "w+")
for el in data_lst:
    for el1 in el:
        write_file.write(el1)
write_file.close()


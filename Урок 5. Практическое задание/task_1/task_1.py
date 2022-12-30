"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

# Creating an empty txt-file
new_file = open("Test_file_N1.txt", "w")

"""# Extracting data from a user ("it works, so commented")
test_data_lst = []
line = "initializing"
while line != "":
    line = input("Enter a next line to record into the file (or just press Enter to finish the operation:\n")
    test_data_lst.append(line)"""

# test array - just to accelerate the debugging
test_data_lst = ["Anchevski", "Dmitri", "Pavlovich", "27/06/1986"]

# Writing the extracted data into the file linebyline
for ln in test_data_lst:
    new_file.write(ln)
    new_file.write('\n')
new_file.close()

# Checking the result
read_file = open("Test_file_N1.txt", "r")
for i, ln in enumerate(read_file):
    print(f"Line {i+1}: {ln}")
read_file.close()
"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

# Test values block
test_num_lst = [5, 4, 3, 2, 1, '15hahaha', 15, 14, 13, 12, 11, 10, 'En12de']  # Numbers to be processed

# (Re)Creating a file
new_file = open("Test_File_N5.txt", "w+")

# Writing data into the (re)created file
for el in test_num_lst:
    new_file.write(f"{el} ")

new_file.close()

# Opening the created file and extracting data out if it
read_file = open("Test_file_N5.txt", "r")
data_str = read_file.read()
data_str = data_str.rstrip(" ")
num_lst = data_str.split(" ")

"""print(f"String - {data_str}")
print(f"List - {num_lst}")"""

# Converting the extracted string number values into float ones
error_lst = []
for i, el in enumerate(num_lst):
    try:
        num_lst[i] = float(el)
    except ValueError:
        error_lst.append([i, el])
        num_lst[i] = None
        continue
# Excluding None-values from the list
if error_lst:
    print("\nThere were incorrect values excluded from the list. They are:")
    for el in error_lst:
        print(el[1])
    for i in range(0, num_lst.count(None)):
        num_lst.remove(None)
    print(f"They are excluded from the list!\n The current list is: {num_lst}")

# Calculating the sum of the remaining values
print(f"The sum is {sum(num_lst)}")
read_file.close()

"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

# Opening a file
read_fl = open("Test_File_N2.txt", 'r')  # opening the file in "read"-mode

# Calculating a number of lines
lines_lst = read_fl.readlines()
print(f"In file {read_fl.name} there are {len(lines_lst)} lines")

# Calculating a number of words in each line
print("Where:")
for i, ln in enumerate(lines_lst):
    temp_lst = ln.split(' ')
    print(f"    In line N{i + 1} there are {len(temp_lst)} words")
read_fl.close()

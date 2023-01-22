"""
Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""


# Class block
class Matrix:
    matrix_lst = []

    def __str__(self):
        res_str = "\r"
        for el in self.cont:
            for el_1 in el:
                res_str += f"{el_1} "
            res_str += "\n"
        return res_str

    def __init__(self, array: list):
        self.rows_num = len(array)
        self.columns_num = len(array[0])
        self.cont = []

        for i in range(0, self.rows_num):
            if len(array[i]) != self.columns_num:
                print(f"Matrix {array} creation canceled! The numbers of elements in rows vary!\n")
                del self
                return None
            for j in range(0, self.columns_num):
                try:
                    array[i][j] = float(array[i][j])
                except ValueError:
                    print(f"Matrix {array} creation canceled! Non-numeric elements were identified!\n")
                    return None

        self.cont = array
        Matrix.matrix_lst.append(self)
        # print(f"Matrix #{Matrix.matrix_lst.index(self)}\n {self}successfully created\n")

    def __add__(self, other):
        # Check block
        # Part 1: Checking the form
        if type(other) != Matrix:
            print("Addition canceled! Attempting to add to a matrix a non-matrix object")
            return None
        if self.columns_num != other.columns_num:
            print("Column number mismatch! Adding matrices of different sizes is not possible")
            return None
        elif self.rows_num != other.rows_num:
            print("Row number mismatch! Adding matrices of different sizes is not possible")
            return None

        # Part 2: Calculation
        res_lst = []
        for i in range(0, self.rows_num):
            res_lst.append(list(self.cont[i]))  # Using additionally "list" to create a separate list of values to avoid
            # the corruption of the initial instances data
            for j in range(0, self.columns_num):
                res_lst[i][j] += other.cont[i][j]
        return Matrix(res_lst)


# Client code block
lst_1 = [['1', '2', '3'], ['4', '5', 6], ['7', 8, 9]]
lst_2 = [[11, '12', 13], [14, 15, '16'], ['17', 18, 19]]
wrong_lst_1 = [[1, 2, 3], [4, 5, 6], [7, 8]]
wrong_lst_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 'd2']]

mtx_1 = Matrix(lst_1)
mtx_2 = Matrix(lst_2)
mtx_wr1 = Matrix(wrong_lst_1)
mtx_wr2 = Matrix(wrong_lst_2)

print("Available matrices:")
for inst in Matrix.matrix_lst:
    print(f"Matrix #{Matrix.matrix_lst.index(inst)}:\n {inst}")

print(f"The combination of matrix mtx_1 and mtx_1 is:\n {mtx_1 + mtx_1}")
print(f"The combination of matrix mtx_1 and mtx_2 is:\n {mtx_1 + mtx_2}")


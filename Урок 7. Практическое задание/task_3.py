"""
Задание 3.

Реализовать программу работы с органическими клетками, состоящими из ячеек.

Необходимо создать класс Клетка (Cell).

В его конструкторе инициализировать параметр (quantity),
соответствующий количеству ячеек клетки (целое число).

В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (add()),
вычитание (sub()),
умножение (mul()),
деление (truediv()).

Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

Сложение. Объединение двух клеток.
При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки.
Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.


** - По желанию: В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****...,
где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.

------------------------------------------------------------------------------
Пример клиентского кода:
print("Создаем объекты клеток")
cell1 = Cell(30)
cell2 = Cell(25)

cell3 = Cell(10)
cell4 = Cell(15)

print()

print("Складываем")
print(cell1 + cell2)

print()

print("Вычитаем")
print(cell2 - cell1)
print(cell4 - cell3)

print()

print("Умножаем")
print(cell2 * cell1)

print()

print("Делим")
print(cell1 / cell2)

print()

print("Организация ячеек по рядам")
print(cell1.make_order(5))
print(cell2.make_order(10))

------------------------------------------------------------------------------
Результаты:
Создаем объекты клеток

Складываем
Сумма клеток = (55)

Вычитаем
Разность отрицательна, поэтому операция не выполняется
Разность клеток = (5)

Умножаем
Умножение клеток = (750)

Делим
Деление клеток = (1)

Организация ячеек по рядам
*****\n *****\n *****\n *****\n *****\n *****\n
**********\n **********\n *****
"""


class Cell:
    cell_lst = []  # An array of all created instances of Cell-class

    def __init__(self, quantity: int):
        try:  # Value check block
            quantity = int(quantity)
        except ValueError:
            print(f"Input data error! '{quantity}' is a non-numeric value of sub-cell quantity")
            return None

        self.quantity = quantity  # Total amount of sub-cells
        self.full_row_num = 1  # After creation a cell is supposed to be formed in 1 row
        self.cells_in_row = quantity  # --"--
        self.unpacked = 0  # --"--
        self.reshaped = False  # A bool attribute to indicate whether the cell was processed by make_order function
        Cell.cell_lst.append(self)  # Adding the created cell to the list

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity < other.quantity:
            print(f"The subtraction from cell N{Cell.cell_lst.index(self)} is cancelled! "
                  f"The subtracted is bigger the reduced")
            return None
        else:
            return Cell(self.quantity - other.quantity)

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        # That was not written in the task, but I believe that should have been!
        # Either division must be greater the zero
        # Or during the division always the greater cell is divided by the lesser cell
        # The first one is more logical, but the second is more interesting - so I make it:
        amax = max(self.quantity, other.quantity)
        amin = min(self.quantity, other.quantity)
        return Cell(amax // amin)

    def __str__(self):
        form = f"Cell N{Cell.cell_lst.index(self)} has: \n {self.quantity} sub-cells\n " \
               f"divided into {self.full_row_num} full rows with {self.cells_in_row} pcs in row\n " \
               f"and {self.unpacked} pcs unpacked\n and looks like:\n"
        if self.reshaped:
            form += f"(The cell was reshaped (by make_order function)\n"
        for i in range(0, self.full_row_num):
            form += "*" * self.cells_in_row + "\n"
        return form + "*" * self.unpacked

    def make_order(self, in_row: int):
        if in_row >= self.quantity:
            print(f"The reshaping of cell N{Cell.cell_lst.index(self)} could not be fulfilled "
                  f"as the set number of sub-cells in row ({in_row}) is not less "
                  f"than the amount of sub-cells in the cell ({self.quantity})")
            return
        self.cells_in_row = in_row
        self.unpacked = self.quantity % in_row
        self.full_row_num = self.quantity // in_row
        self.reshaped = True
        return


# Client code
init_lst = [30, 50, 60, 6, '13', '3f1']  # initial data list (quantities for cell creation)

for el in init_lst:  # Creating cells (the last should not be created because of the erroneous value)
    Cell(el)

# Fulfilling the operations (including erroneous)
Cell.cell_lst[0] - Cell.cell_lst[1]  # Subtraction mistake
Cell.cell_lst[1] - Cell.cell_lst[0]  # cell[5] 20
Cell.cell_lst[2] + Cell.cell_lst[3]  # cell[6] 66
Cell.cell_lst[4] * Cell.cell_lst[4]  # cell[7] 169
Cell.cell_lst[1] / Cell.cell_lst[3]  # cell[8] 8
Cell.cell_lst[3] / Cell.cell_lst[4]  # cell[9] 2 (because of reversing elements' positions when divider is greater)

Cell.cell_lst[6].make_order(10)  # 6*10 + 6
Cell.cell_lst[7].make_order(15)  # 11*15 + 4
Cell.cell_lst[9].make_order(4)   # not reshaped

for el in Cell.cell_lst:
    print(f"{el}")




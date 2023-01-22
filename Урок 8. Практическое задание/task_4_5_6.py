"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над четвертым заданием.
Разработать методы, отвечающие за приём оргтехники на
склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над пятым заданием. Р
еализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


# Import Block
from abc import ABC
from random import randint

# End of Import block


# Classes block
class OnlyDigitsValue(Exception):
    def __init__(self, value):
        print(f"You've entered a non-numeric value: {value} of type {type(value)}")


class Department:
    """ Just a piece of a Class to follow the OOP conception"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"


class Warehouse:

    def __init__(self, name, departments: list):
        self.name = name
        self.eq_indexes = [self.name, 0]
        self.journal = {"Warehouse": []}  # The first category - is Warehouse itself
        # All the equipment accepted to the warehouse will be first kept in the value-list for the key "Warehouse"
        for department in departments:  # All the department of the company to be serviced are added to the
            # "journal"-dictionary (during the initiation - without any equipment)
            self.journal.update({department: []})
        self.eq_dict = {}
        print(f"Warehouse {self.name} is created!")

    def add_department(self, department_to_add):  # Now - just a plug
        pass

    def remove_department(self, department_to_remove):  # Now - just a plug
        pass

    def __str__(self):
        ret_str = f"Warehouse {self.name} serves the next departments: "  # Preparing the return string
        deps_served = list(self.journal.keys())
        deps_served.remove("Warehouse")
        for dep_served in deps_served:  # Extracting departments' names
            ret_str += f"{dep_served}; "  # And adding them to the return string
        ret_str += f"\nIn the warehouse {self.name} the following equipment is kept: "
        ware_eq = self.journal.get("Warehouse")
        if ware_eq:  # Not to raise TypeError because of NoneType non iterability
            for ware_eq_i in ware_eq:
                ret_str += f"{ware_eq_i}; "
        else:
            ret_str += "None"
        return ret_str

    def accept_oe(self, equipment):
        """ Adding a new equipment unit into the warehouse"""
        if not isinstance(equipment, OfficeEquipment):  # Checking for the data compliance
            print(f"Unknown type of equipment! Acceptance aborted")
        extr_list = self.journal.get("Warehouse")  # Extracting existing list of the equipment available in the WH
        extr_list.append(equipment)  # ...and it suprisingly turned to be automatically changing the DICTIONARY!!!
        equipment.location = self.name  # In the equipment data its location is set as this warehouse's name
        equipment.index = list(self.eq_indexes)  # The same is with its indexes

        # self.journal["Warehouse"] = extr_list  # It was supposed to be Rewriting the list to the Dictionary
        # But it turned out to be unnecessary!!! Because changing 'extr_list' automatically changes the dictionary

        print(f"{equipment} is accepted to {self.name}")
        self.eq_indexes[1] += 1  # Incrementing the "free" index (for a perspective equipment to be accepted)

    def transfer(self, equipment, department: Department):  # Sure, department also ought to be a Class (but not in the
        """ Transferring a unit available in the warehouse to a given department """
        available_eq = self.journal.get("Warehouse")  # Downloading the available units' list
        # Checking for availability of the given equipment unit in the warehouse
        if equipment not in available_eq:
            print(f"Chosen office equipment '{equipment.getdata}' is not available in the warehouse!")
            if equipment.location:
                print(f"Chosen equipment '{equipment.getdata}'is already moved to '{equipment.location}'")
            else:
                print(f"The location of {equipment} is unknown!!!")
            return None
        else:
            # Removing the given equipment unit from the warehouse balance:
            available_eq.remove(equipment)
            # self.journal["Warehouse"] = available_eq  # Also turned to be unnecessary
            # Adding the equipment unit to the given department
            dep_eq = self.journal.get(department)  # Extracting available
            dep_eq.append(equipment)  # Replenishing with the new
            # self.journal[department] = dep_eq  # Rewriting to the Dict (but an unnecessary action)
            print(f"Equipment '{equipment}' was attached to the '{chosen_dep}'")
            equipment.location = department

    @property
    def check_out(self):
        """ Gives the statistics of how many items of every type of equipment is available in the warehouse"""
        in_warehouse = list(self.journal.get("Warehouse"))  # If not using "list()" then
        # popping an item from in_warehouse will somehow pop it also from the self.journal... Why???
        # I thought 'get()' automatically creates a separate list///
        i = 0
        while i < len(in_warehouse):
            count = 1
            j = i + 1
            self.eq_dict.update({str(in_warehouse[i]): count})
            while j < len(in_warehouse):
                if str(in_warehouse[j]) == str(in_warehouse[i]):
                    count += 1
                    self.eq_dict.update({str(in_warehouse[i]): count})
                    in_warehouse.pop(j)
                    j -= 1
                j += 1
            i += 1
        return self.eq_dict


class OfficeEquipment:
    oe_lst = []  # All created instances of office equipment are registered in this list

    @staticmethod
    def mass_create(name, amount):
        """ Creates a number of instances with the same name (just to fit the task)"""
        try:  # Using Exceptions (just to fit the task)
            if type(amount) != int:
                raise OnlyDigitsValue(amount)
        except OnlyDigitsValue as odv:
            return
        for i in range(0, amount):
            print(f"{OfficeEquipment(name).name} has been created")

    def __init__(self, name):
        self.name = name
        OfficeEquipment.oe_lst.append(self)
        self.location = None
        self.index = []

    def __str__(self):
        """ Now only name is necessary when printing an item"""
        return f"{self.name}"

    @property
    def getdata(self):
        """ This one - to print the full information about the unit"""
        return f"{self.name}-{self.index}-{self.location}"


class Printer(OfficeEquipment):
    printers_lst = []  # All created instances of printers are registered in this list

    def __init__(self, color_type, toner_type, name):
        self.color_type = color_type
        self.toner_type = toner_type
        super().__init__(name)
        Printer.printers_lst.append(self)

    def __str__(self):
        return f"{self.name}-{self.toner_type}-{self.color_type}"

    @property
    def getdata(self):
        return f"{self.name}-{self.toner_type}-{self.color_type}-{self.index}-{self.location}"


class Scaner(OfficeEquipment):
    """ Now - just to fit the task - without a proper reloading and redetermination"""
    def __init__(self, flow_type, name):
        self.flow_type = flow_type
        super.__init__(name)


class Copier(OfficeEquipment):
    """ Now - just to fit the task - without a proper reloading and redetermination"""
    def __init__(self, color_type, flow_type, name):
        self.color_type = color_type
        self.flow_type = flow_type
        super.__init__(name)


# Client code
# _Test block
# __ Departments data (not from the task)
departments_data = ["PAD", "CDD", "PTD", "SD"]
dep_list = []
for i, dep in enumerate(departments_data):
    dep_list.append(Department(dep))
# __ End of Departments

# __ Printers test data
printers_data_lst = [["Color", "Laser", "HP"], ["Black", "Laser", "Epson"], ["Color", "Ink", "Cannon"],
                     ["Color", "Laser", "HP"], ["Color", "Laser", "HP"], ["Black", "Laser", "Epson"]]


# Initiation block
# Creating a warehouse:
warehouse_1 = Warehouse("WH1", dep_list)
print(warehouse_1)

# Creating some printers
for pr in printers_data_lst:
    Printer(pr[0], pr[1], pr[2],)
print(f"\nThe next printers were created:")
for printer in Printer.printers_lst:
    print(printer)

# Accepting printers into the warehouse
print(f"\nAccepting printers to the warehouse:")
for pr in Printer.printers_lst:
    warehouse_1.accept_oe(pr)

# Inquiring warehouse data
print(f"\nThis is the warehouse {warehouse_1.name} data (through 'check_out'-function: ")
for el in warehouse_1.check_out.items():
    print(f"{el[0]} - {el[1]} p.")

# Moving printers to the departments
print(f"\nMoving equipment to random departments:")
for eq in OfficeEquipment.oe_lst:
    chosen_dep = dep_list[randint(0, len(dep_list)-1)]
    warehouse_1.transfer(eq, chosen_dep)

# Checking the printers data after the move
print("\nReading the printers aftermove-data")
for pr in Printer.printers_lst:
    print(f"{pr}: index {pr.index}, location: {pr.location}")

# Trying to move an already moved equipment
warehouse_1.transfer(OfficeEquipment.oe_lst[0], dep_list[1])  # Not available!

# Trying to mass-create some equipment units
OfficeEquipment.mass_create("NewEquipment", 5)

# Trying to mass-create some equipment units with erroneous 'amount' value
OfficeEquipment.mass_create("NewEquipment2", '2')  # Error! V

print("\nAll the created equipment")
for oe in OfficeEquipment.oe_lst:
    print(f"  - {oe.getdata}")


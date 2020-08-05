"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
 а также других данных, можно использовать любую подходящую структуру, например словарь.
"""
"""
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
 изученных на уроках по ООП.
"""

from Lesson_08.Task_04 import Warehouse, TypeEquipments, Equipment
from enum import Enum

class CompanyDirections(Enum):
    warehouse = "Склад"
    office = "Склад"

class Office:
    currentItems = []

class userExeptionNotFoundId(Exception):
    errorName = "Оборудование не найдено"

class userExeptionNotEnoughSize(Exception):
    maxSize: int
    errorName = ""
    def __init__(self, size: Warehouse.maxSizePlaceSM):
        self.maxSize = size
        self.errorName = f"Оборудование больше возможного размера хранимого оборудования ({self.maxSize})"

class Operations():
    @classmethod
    def moveEqupment(cls, office: Office, warehouse: Warehouse,
                     equipmentID: int, targetTo: CompanyDirections):
        if targetTo == CompanyDirections.office:
            found = False
            indexEq = None
            for num in warehouse.currentItems:
                if num.id == equipmentID:
                    indexEq = warehouse.currentItems.index(num)
                    found = True
            if not found:
                raise userExeptionNotFoundId
            elif found:
                office.currentItems.append(warehouse.currentItems[indexEq])
                del warehouse.currentItems[indexEq]
                print("Success")

# check Task

newWarehouse = Warehouse()
newOffice = Office()

newWarehouse.currentItems.append(Equipment(200,[20,40,50], 122, TypeEquipments.copier))
newWarehouse.currentItems.append(Equipment(200,[50,40,50], 130, TypeEquipments.printer))
print(f"кол-во текущего оборудования на складе: {len(newWarehouse.currentItems)}")
Operations.moveEqupment(newOffice, newWarehouse, 122, CompanyDirections.office)
print(f"кол-во текущего оборудования на складе после операции: {len(newWarehouse.currentItems)}")
print(f"кол-во текущего оборудования в офисе после операции: {len(newOffice.currentItems)}")
"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from enum import Enum

class TypeClouth(Enum):
    coat = "пальто"
    suit = "костюм"

class clothProduct:
    def __init__(self, name: str, type: TypeClouth, sizeV: float, heightH: float):
        self.name = name
        self.type = type
        self.sizeV = sizeV
        self.heightH = heightH

    @property
    def valueClouth(self):
        if self.type == TypeClouth.coat:
            return (self.sizeV/6.5 + 0.5)
        elif self.type == TypeClouth.suit:
            return (2*self.heightH + 0.3)

someCoat = clothProduct("Бабушкино пальто", TypeClouth.coat, 44, 170)
print(someCoat.valueClouth)
someSuit = clothProduct("Дедушкин костюм", TypeClouth.suit, 44, 170)
print(someSuit.valueClouth)
"""
4.Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""

from enum import Enum

class Direction(Enum):
    left = "Влево"
    right = "Вправо"
    straight = "Прямо"
    back = "Назад"

from enum import Enum

class ClassCar(Enum):
    VIP = 1
    A = 2
    B = 3
    C = 4

class Car:
    speed: int
    color: str
    is_police: bool
    direction: Direction
    def go(self):
        print("Машина начала движение")
    def stop(self):
        print("Машина остановилась")
    def turn(self):
        print(f"Машина движется по направлению {self.direction.value}")
    def show_speed(self):
        print(f"Текущая скорость {self.speed}")

    def __init__(self, speed, color, is_police, direction):
        self.speed = speed
        self.color = color
        self.is_police = is_police
        self.direction = direction


class TownCar(Car):
    rentaCar: bool = False
    classCar: ClassCar

    def __init__(self, classCar):
        self.classCar = classCar

    def show_speed(self):
        print(f"Текущая скорость {self.speed}")
        if self.speed > 60:
            print("Вы нарушаете скоростной режим")

class SportCar(Car):
    rallyCar: bool = False

class WorkCar(Car):
    cargoValueM: int

    def __init__(self, speed, color, is_police, direction, cargoValueM):
        super().__init__(speed, color, is_police, direction)
        self.cargoValueM = cargoValueM

    def show_speed(self):
        print(f"Текущая скорость {self.speed}")
        if self.speed > 40:
            print("Вы нарушаете скоростной режим")

class PoliceCar(Car):
    pass

someSportCar = SportCar(100, "red", True, Direction.straight)
someSportCar.turn()

someWorkCar = WorkCar(70, "yellow", False, Direction.right, 200)
someWorkCar.show_speed()

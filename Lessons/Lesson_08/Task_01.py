"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

import datetime
import time

class Date:
    @classmethod
    def dateInt(cls, dateStr: str):
        if cls.validationDate(dateStr):
            date: list = dateStr.split("-")[::-1]
            date = list(map(int, date))
            dateDateFormat = datetime.date(date[0], date[1], date[2])
            resultSecond = time.mktime(dateDateFormat.timetuple())
            return (resultSecond)
        return None

    @staticmethod
    def validationDate(dateStr: str):
        try:
            date: list = dateStr.split("-")
            date = list(map(int, date))
            if 0 < date[0] < 32:
                if 0 < date[1] < 13:
                    if 1970 < date[2] < 2099:
                        return True
        except:
            return False


print(Date.dateInt("01-05-2020"))


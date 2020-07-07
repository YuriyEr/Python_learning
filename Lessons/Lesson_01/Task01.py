# Задание 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

# явное задание типа (нестрогая типизация)
value_one: int = 10 + 1
print(value_one)

# явное указание типа все равно позволяет переопределять тип впоследствии
value_one = "some text"
print(value_one)

# безопасное преобразование через отлов ошибок
someValueInput = 100

try:
    int(someValueInput)
    print("успешно")
except:
    print("ошибка приведения типа")

# запрос ввода с клавиатуры с безопасным извлечением
valueInput = input("Введите любое значение >> ")
valueType: str
try:
    if isinstance(int(valueInput), int):
        valueType = "integer"
        print("ваше выражение {} является типом {}".format(valueInput, valueType))
except:
    valueType = "string"
    print("ваше выражение {} является типом {}".format(valueInput, valueType))
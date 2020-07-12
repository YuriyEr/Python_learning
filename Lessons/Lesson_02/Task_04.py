# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

# someInput = input("Напишите любое предложение\n")

# someInput = "Маша любит Сашу и СамантуРитуДжонс"
someInput = input("Введите произворльное предложение \n")

someList = []
buffer = ""

for value in someInput:
    if value != " ":
        buffer = buffer + value
    else:
        if len(buffer) > 10:
            newBuffer = ""
            for value in range(0,10):
                newBuffer = newBuffer + buffer[value]
                someList.append(newBuffer)
                buffer = ""
        else:
            someList.append(buffer)
            buffer = ""

if buffer != " " and buffer != "":
    if len(buffer) > 10:
        newBuffer = ""
        for value in range(0, 10):
            newBuffer = newBuffer + buffer[value]
        someList.append(newBuffer)
        buffer = ""
    else:
        someList.append(buffer)
        buffer = ""

print("Результат упражнения")
for key, result in enumerate(someList):
    print(f"{key+1} {result}")
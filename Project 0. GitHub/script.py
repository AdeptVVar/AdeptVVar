import numpy as np

count = 1  # счетчик попыток
number = np.random.randint(1, 101)  # загадали число
predict = 1 # предполагаемое число
while True:  # бесконечный цикл
    if number == predict:
        break  # выход из цикла, если угадали
    elif number > predict:
        predict += 10
        count += 1  # плюсуем попытку
    elif number < predict:
        predict -= 1
        count += 1  # плюсуем попытку

print(f"Вы угадали число {number} за {count} попыток.")
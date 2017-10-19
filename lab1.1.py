import math

tmpn = input("Введите N: ")
n = int(tmpn)
result = []
result.append(2)

for i in range(3, n + 1):
    tmp = True
    for element in result:
        if(i % element == 0):
            tmp = False
            break
    if(tmp):
        result.append(i)
        print(i)
        

lenght = len(result)
print("\nКоличество простых чисел: ", lenght)

adamar = math.floor(n / (math.log(n)))
print("Оценка по формуле Адамара: ", adamar)
print("Погрешность: ", round(math.fabs(lenght - adamar) * 100 / lenght, 2), "%")

const_k = 1.08633
lagrange = math.floor(n / (math.log(n) - const_k))
print("Оценка по формуле Лагранжа: ", lagrange)
print("Погрешность: ", round(math.fabs(lenght - lagrange) * 100 / lenght, 2), "%")

import random

nbers = [0] * 20 #список кортежей
unique = [] #список уникальных пар
k = 0 #кол-во пар, чья сумма < n
for j in range(20): #заполнение списка и кортежей рандом числами
    nbers[j] = tuple(sorted([random.randint(-10, 10) for i in range(4)]))  
for j in nbers: #проверяется уникальность пар, добавляется в список уникальных пар
    if nbers.count(j)==1:
        unique.append(j)
print("Все уникальные пары: ", unique) #вывод уникальных пар
n = int(input("\nВведите целое число: ")) #ввод n
for j in nbers: # находится кол-во пар, чья сумма меньше n
    k +=(1 if j[0] + j[1] + j[2] + j[3] < n else 0)
print(f"Количество пар, чья сумма < {n} = {k}") #вывод кол-ва

# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list = [6, -6, 1, 5, -9, 10, 2, 4, -10, -5, 6, -2, 3, 7, -7, 8, -4, 9, -3, -1, -8, 0]
print(list)
mini = int(input("Введите минимальное значение диапазона: "))
maxi = int(input("Введите максимальное значение диапазона: "))
list_index = []
for i in range(len(list)):
    if mini <= list[i] <= maxi:
        list_index.append(i)
print(list_index)
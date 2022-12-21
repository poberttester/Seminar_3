# Задан список из нескольких чисел. Программа найдёт сумму элементов списка, стоящих на нечётной позиции.

list1 = [2, 3, 4, 34, 5, 10]
summ = 0

for index,value in enumerate(list1):
	if (index % 2) != 0:
		summ += list1[index]

print(summ)
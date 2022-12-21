# Программа найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

listik = [12, 34, 42, 234, 13, 43]
product_of_numbers = []


for i, first in enumerate(listik):

	if i >= len(listik) - 1 - i:
		break

	second = listik[len(listik) - 1 - i]
	product_of_numbers.append(first * second)
	
print(product_of_numbers)





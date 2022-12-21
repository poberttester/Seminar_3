# Задан список из вещественных чисел. Программа найдёт разницу между максимальным и минимальным значением дробной части элементов.

listic = [1.1, 1.2, 3.1, 5, 10.01]
min = 1		# 1 - дробь не может быть больше этого числа (максимальное значение)
max = 0		# 0 - дробь не может быть меньше этого числа (минимальное значение)
temp_int, temp_float = None, None

for i, value in enumerate(listic):
	temp_int = int(value)
	temp_float = round(value - temp_int, 2)
	
	if temp_float != 0:		# нельзя допустить, чтобы дроби сравнивались с нулём
		 
		if temp_float > max:
			max = temp_float

		if temp_float < min:
			min = temp_float

# Ответ
print(max - min)

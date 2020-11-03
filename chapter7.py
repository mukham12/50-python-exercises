def join_numbers(numbers):
	return ','.join(str(number) for number in numbers)


print(join_numbers(range(15)))

def join_numbers(numbers):
	return ','.join(str(number) for number in numbers)


print(join_numbers(range(15)))


def sum_numbers(numbers):
	"""
	Write a function that sums the digits of the given string which could potentially contain anything besides digits.
	:param numbers:
	:return:
	"""
	return sum(int(number) for number in numbers.split() if number.isdigit())


print(sum_numbers('1 2 3 a b c 4'))


def flatten(l):
	"""
	Write a function that takes a list of lists (just one element deep)
	and returns a flat, one-dimensional version of the list
	:param l: 2D-list
	:return: list
	"""
	return [element for sublist in l for element in sublist]


print(flatten([[1, 2], [3, 4]]))

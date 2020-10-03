def firstlast(iterable):
	"""
	Exercise 3.1
	Write a function that takes in an iterable and returns
	the first and the last elements appended to a new collection of that type
	:param iterable: an iterable of anything
	:type iterable: object
	"""
	return iterable[:1] + iterable[-1:]


# A few test cases to check whether the function written above is working correctly.
print(' ' * 14, 'Exercise 1', ' ' * 22, '*')
print(firstlast([1, 2, 3, 4]), ' ' * 41, '*')  # Expected output: [1, 4]
print(firstlast('abc'), ' ' * 45, '*')  # Expected output: ac
print(firstlast((3, 5, 1, 4)), ' ' * 41, '*')  # Expected output: (3, 4)
print('*' * 50)


# Extension from the previous exercise
def even_odd_sum(iterable):
	"""
	Iterate over the iterable such as a list or a tuple, add all of the numbers that are located in even
	indices and odd indices and return a list with such that [sum_odd, sum_even]
	:param iterable: object
	:return: list
	"""
	output = [0, 0]
	for i, number in enumerate(iterable):
		if i % 2 != 0:
			output[1] += number
		else:
			output[0] += number
	return output


# A few test cases to check whether the function written above is working correctly.
print(' ' * 14, 'Exercise 2', ' ' * 22, '*')
print(even_odd_sum([10, 20, 30, 40, 50, 60]), ' ' * 38, '*')  # Expected output: [90, 120]
print(even_odd_sum((18, 6, 90, 35, 30, 36, 14)), ' ' * 38, '*')  # Expected output: [152, 77]
print(even_odd_sum([68, 70, 24, 49, 86, 26, 91, 38, 4]), ' ' * 37, '*')  # Expected output: [273, 183]
print('*' * 50)


# Extension exercise to the first exercise
def plus_minus(iterable):
	"""
	Iterate over the array and add/subtract a number from a total depending on the
	index the number is located in, namely if the number is located on an even index,
	it has to be added to the total otherwise it has to be subtracted but first number is an exception.
	:param iterable:
	:return: int
	"""
	total = iterable[0]
	for i, number in enumerate(iterable[1:]):
		if i % 2 == 0:
			total = total + number
		else:
			total = total - number
	return total


# A few test cases to check whether the function written above is working correctly.
print(' ' * 14, 'Exercise 3', ' ' * 22, '*')
print(plus_minus([10, 20, 30, 40, 50, 60]), ' ' * 45, '*')  # Expected output: 50
print(plus_minus((8, 68, 46, 85, 16, 96, 58, 23)), ' ' * 44, '*')  # Expected output: 160
print(plus_minus([25, 49, 67, 85, 86]), ' ' * 46, '*')  # Expected output: 6
print('*' * 50)


def my_sum(*items):
	"""
	Extending the function I wrote in Chapter 1 to be able to sum everything from strings to other iterables.
	If the given parameters are digits then it returns the sum, if it is a collection then everything is
	appended into collection.
	:param items:
	:return: iterable
	"""
	if not items:
		return items
	output = items[0]
	for item in items[1:]:
		output = output + item
	return output


# A few test cases to check whether the function written above is working correctly.
print(' ' * 14, 'Exercise 4', ' ' * 22, '*')
print(my_sum(), ' ' * 45, '*')
print(my_sum(10, 20, 30, 40), ' ' * 44, '*')
print(my_sum('a', 'b', 'c', 'd'), ' ' * 43, '*')
print(my_sum([10, 20, 30], [40, 50, 60], [70, 80]), ' ' * 15, '*')
print('*' * 50)


# Extension function to the above exercise
def sum_numeric(*items):
	"""
	Write a function that takes any number of arguments.
	If the argument is or can be turned into an integer, then it should be
	added to the total. Arguments that can't be handled as integers should be ignored.
	:param items: any
	:return: int
	"""
	total = 0
	for item in items:
		try:
			total = total + int(item)
		except ValueError:
			pass
	return total


# A few test cases to check whether the function written above is working correctly.
print(' ' * 14, 'Exercise 4', ' ' * 22, '*')
print(sum_numeric(10, 20, 'a', '30', 'bcd'), ' ' * 45, '*')  # Expected output: 60
print(sum_numeric('55', 20, 'abcd', '32', '3'), ' ' * 44, '*')  # Expected output: 110
print(sum_numeric('15', '20', 'a', '35', 'bcd'), ' ' * 45, '*')  # Expected output: 70
print(sum_numeric(31, 43, 41, 26, 39, 13, 'ab'), ' ' * 44, '*')  # Expected output: 193
print('*' * 50)

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
print(firstlast([1, 2, 3, 4]))  # Expected output: [1, 4]
print(firstlast('abc'))  # Expected output: ac
print(firstlast((3, 5, 1, 4)))  # Expected output: (3, 4)


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
print(even_odd_sum([10, 20, 30, 40, 50, 60]))  # Expected output: [90, 120]
print(even_odd_sum((18, 6, 90, 35, 30, 36, 14)))  # Expected output: [152, 77]
print(even_odd_sum([68, 70, 24, 49, 86, 26, 91, 38, 4]))  # Expected output: [273, 183]

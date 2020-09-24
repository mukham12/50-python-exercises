# Exercise 2
def custom_sum(*numbers):
	"""
	Recreate the sum function that accepts many values as a parameter instead of
	accepting a list of numbers
	"""
	total = 0
	for number in numbers:
		total = total + number
	return total


# A few test cases for the above function
print(custom_sum(1, 2, 3, 4, 5))  # Has to print out 15
print(custom_sum(2, 9, 10, 11))  # Has to print out 32
print(custom_sum(21, 8, 16, 1))  # Has to print out 46

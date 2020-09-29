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

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


def flatten_odd_ints(l):
	"""
	Write a function that is almost identical to flatten written above but this function is going to
	return a flattened list of only odd integers and nothing else.
	:param l: 2D-list
	:return: list
	"""
	return list(filter(lambda x: x % 2, [element for sublist in l for element in sublist]))


print(flatten_odd_ints([[1, 2], [3, 4]]))


def plword(word):
	"""
	Write a function that takes a filename as an argument. It returns a string with the file’s contents, but with each word translated into Pig Latin
	:param word: string
	:return: string
	"""
	return word + 'way' if word[0] in 'aeiou' else word[1:] + word[0] + 'ay'


def plfile(filename):
	return ' '.join(plword(one_word) for one_line in open(filename) for one_word in one_line.split())


def flipped_dict(dictionary):
	"""
	Write a function that will flip the dictionary.
	:param dictionary: dict
	:return: dict
	"""
	return {value: key for key, value in dictionary.items()}


print(flipped_dict({'a': 1, 'b': 2, 'c': 3}))

import string


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


def transform_values(function, dictionary):
	"""
	In this exercise, create a slight variation on 'map', one that applies a function to each of the values of a dict.
	The result of invoking this function, is a new dict whose keys are the same as the input dict, but whose values
	have been transformed by the function.
	:param function: A function
	:param dictionary: A dictionary
	:return: A dictionary
	"""
	return {key: function(value) for key, value in dictionary.items()}


d = {'a': 1, 'b': 2, 'c': 3}
print(transform_values(lambda x: x * x, d))


def get_sv(filename):
	"""
	Write a function that returns a set of all “supervocalic” words in the dict. Simply put, supervocalic words contain
	all five vowels in English (a, e, i, o, and u), each of them appearing once and in alphabetical order.
	For the purposes of this exercise, accepting any word that has all five vowels, in any order and any number of times.
	The function should find all of the words that match this definition (i.e., contain a, e, i, o, and u) and return a
	set containing them.
	:param filename: Name of the file
	:return: set
	"""
	return {word.strip() for word in open(filename) if {'a', 'e', 'i', 'o', 'u'} < set(word.lower())}


def gematria_dict():
	"""
	Write a function that numbers all the lowercase letters of the English alphabet and numbers them from 1 to 26.
	The return type is a dictionary so the keys are the letters and the values are the numbers.
	:return: dict
	"""
	return {char: index for index, char in enumerate(string.ascii_lowercase, 1)}


print(gematria_dict())

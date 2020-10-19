from collections import defaultdict
from io import StringIO

fakefile = StringIO('''
nobody:*:-2:-2::0:0:Unprivileged User:/var/empty/:/usr/bin/false
root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false
''')


def get_final_line(filename):
	"""
	Write a function that returns the final line of any given file, in other words, a function that
	is similar to Unix head and tail utilities.

	:param filename: path to the file
	:return: final line of the file
	"""
	final_line = ''
	for current_line in fakefile:  # Change fakefile to actual filename passed in as argument
		final_line = current_line
	return final_line


print(get_final_line('/etc/passwd'))

fake_vowels = StringIO('''This is just a test to see if the function implemented
						above is correctly counting the vowels appearing in this text''')


# Beyond exercise problem
def count_vowels_file(filename):
	count = defaultdict(lambda: 0)
	for line in fake_vowels:
		for character in line:
			if character in 'aeiou':
				count[character] += 1

	for key, value in count.items():
		print(key, ' ' * 10, value)
	return ''


print(count_vowels_file(''))


# Exercise 19
def password_to_dict(filename):
	"""
	Write a function that reads from from a Unix-style "password file," commonly stored as /etc/passwd, and returns
	a dictionary based on it.
	:param filename: name of the file
	:return: dict
	"""
	users = {}
	with open(filename) as password:
		for line in password:
			if not line.startswith(('#', '\n')):
				user_information = line.split(':')
				users[user_information[0]] = int(user_information[2])
	return users


print(password_to_dict('/etc/passwd'))


def wordcount(filename):
	counts = {'Characters': 0, 'Words': 0, 'Lines': 0}
	unique_words = set()

	for line in open(filename):
		counts['lines'] += 1
		counts['characters'] += len(line)
		counts['words'] += len(line.split())

		unique_words.update(line.split())
	counts['Unique words'] = len(unique_words)

	for key, value in counts.items():
		print(f'{key}: {value}')


wordcount('sample_file.txt')

import operator
import random


def myxml(tagname, content='', **kwargs):
	"""
	Write a function that allows you to create simple XML output.
	The output from the function will always be a string.
	:param tagname: name of the tag
	:param content: what is enclosed between XML tags
	:return: XML output
	"""
	attrs = ''.join([f' {key}="{value}"' for key, value in kwargs.items()])
	return f'<{tagname}{attrs}>{content}</{tagname}>'


print(myxml('foo', 'hello', a=1, b=2, c=3))


def calc(to_solve):
	operators = {'+': operator.add,
	             '-': operator.sub,
	             '*': operator.mul,
	             '/': operator.truediv,
	             '**': operator.pow,
	             '%': operator.mod}
	op, first_s, second_s = to_solve.split()

	first = int(first_s)
	second = int(second_s)

	return operators[op](first, second)


print(calc('+ 2 3'))


def create_password_generator(characters):
	"""
	Write a function that generates a random password from the given characters.
	:param characters: a string of characters
	:return: random password
	"""

	def create_password(length):
		output = []
		for _ in range(length):
			output.append(random.choice(characters))
		return ''.join(output)

	return create_password


alpha_password = create_password_generator('abcdef')
symbol_password = create_password_generator('!@#$%')

print(alpha_password(5))
print(alpha_password(10))

print(symbol_password(5))
print(symbol_password(10))

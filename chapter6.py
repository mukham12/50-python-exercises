import operator


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

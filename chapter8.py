def menu(**options):
	while True:
		option_string = ' / '.join(sorted(options))
		choice = input(f'Enter an option ({option_string}): ')
		return options[choice]() if choice in options else 'Not a valid option'


def func_a():
	return 'A'


def func_b():
	return 'B'


return_value = menu(a=func_a, b=func_b)
print(f'Result is {return_value}')

MENU = {'sandwich': 10, 'tea': 7, 'salad': 9}


def restaurant():
	"""
	Exercise 1

	Write a function that prompts the user to enter a name of a dish from restaurant menu.
	If the name entered exists within the dictionary, retrieve and display the price and
	add the price to the total. Keep asking user until empty string is entered.
	:return: string
	"""
	total = 0
	while True:
		order = input('Order: ').strip()
		if not order:
			break

		if order in MENU:
			total = total + MENU[order]
			print(f'order is {MENU[order]}, total is {total}')
		else:
			print(f'We are fresh out of {order} today')

	print(f'Your total is {total}')


restaurant()

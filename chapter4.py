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


def get_rainfall():
	"""
	Write a function that tracks rainfall in a number of cities. Users will enter the name of a city,
	if the city name is blank, then the function prints a report before exiting. If the city name isn’t blank, then the
	program should also ask the user how much rain has fallen in that city. After the user enters the quantity of rain,
	the program again asks them for a city name, rainfall amount, and so on--until the user presses Enter instead of
	typing the name of a city. When the user enters a blank city name, the program exits--but first, it reports how much
	total rainfall there was in each city.

	:return: string
	"""
	rainfall = {}
	while True:
		name = input('Enter city name: ')
		if not name:
			break

		mm_rain = input('Enter how much rain has fallen in mm: ')
		rainfall[name] = rainfall.get(name, 0) + int(mm_rain)

	for city, rain in rainfall.items():
		print(f'{city}: {rain}')


get_rainfall()

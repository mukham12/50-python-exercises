from decimal import Decimal

rates = {
	'Chico': Decimal('0.5'),
	'Groucho': Decimal('0.7'),
	'Harpo': Decimal('0.5'),
	'Zeppo': Decimal('0.4')
	}


def time_percentage(hour):
	return hour / Decimal('24.0')


def calculate_tax(amount, state, hour):
	return float(amount + (amount * rates[state] * time_percentage(hour)))

from random import randint

rand_number = randint(1, 10)

# Exercise 1.2
while True:
	"""
	Create a number guessing program that generates a pseudorandom number,
	asks the user what their guess is and returns the result accordingly.
	Also, the displays are color coded to make it easier to see!
	"""
	try:
		guess = int(input('Try to guess a number between 1 and 10: '))
		if guess <= 0 or guess > 10:
			raise ValueError
	except ValueError:
		print('\u001b[31m\nEnter a valid number please!\n\033[0m')
		continue
	if guess == rand_number:
		print(f'\033[0;32m\nYou got it right, the number was {rand_number}\033[0m')
		break
	elif guess < rand_number:
		print('\033[1m\033[4m\nToo low, try a different number!\n\033[0m')
		continue
	else:
		print('\033[1m\033[4m\nToo high, try a different number!\n\033[0m')
		continue


# Exercise 1.3
def custom_sum(*numbers):
	"""
	Recreate the sum function that accepts many values as a parameter instead of
	accepting a list of numbers
	"""
	total = 0
	for number in numbers:
		total = total + number
	return total


# A few test cases for the sum function implemented above
print(custom_sum(1, 2, 3, 4, 5))  # Has to print out 15
print(custom_sum(2, 9, 10, 11))  # Has to print out 32
print(custom_sum(21, 8, 16, 1))  # Has to print out 46



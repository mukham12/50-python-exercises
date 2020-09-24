from random import randint

rand_number = randint(1, 10)

while True:
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

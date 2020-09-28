"""
Exercise 2.1
Write a Pig Latin game.
Pig Latin is a common children’s "secret" language in English-speaking countries.
Rules are:
1. If a word begins with a vowel then append "way" to the end of the word.
2. Otherwise, take out the first letter of the word, add it to the end of the word with "ay" attached to it.
"""
word = input('Enter a word: ')
if word[0] in 'aeiou':
	print(f'{word}way')
else:
	print(f'{word[1:]}{word[0]}ay')

# Exercise 2.3
# Pig Latin but instead of a word, now we are asking for sentences as an input!
for word in input('Enter a sentence: ').split():
	if word[0] in 'aeiou':
		print(f'{word}way', end=' ')
	else:
		print(f'{word[1:]}{word[0]}ay', end=' ')

'''
Alternative version, shorter but probably less readable
for word in input('Enter a sentence: ').split():
	print(f'{word}way', end=' ') if word[0] in 'aeiou' else print(f'{word[1:]}{word[0]}ay', end=' ')
'''
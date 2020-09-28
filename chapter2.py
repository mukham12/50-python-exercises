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

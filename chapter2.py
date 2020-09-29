'''
Exercise 2.1
Write a Pig Latin game.
Pig Latin is a common children’s "secret" language in English-speaking countries.
Rules are:
1. If a word begins with a+ vowel then append "way" to the end of the word.
2. Otherwise, take out the first letter of the word, add it to the end of the word with "ay" attached to it.
'''
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

'''
Exercise 2.4 (Ubbi Dubbi)
Ubbi dubbi is a language game spoken with the English language.
It was popularized by the 1972-1978 PBS children's show Zoom.
When Zoom was revived in 1999 on PBS, Ubbi dubbi was again a feature of the show.
						RULES
Ubbi dubbi works by adding -ub- before each vowel sound in a syllable.

Alternative version, shorter but probably less readable
for letter in input("Enter a word: "):
    print(f'ub{letter}', end='')  if letter in 'aeiou' else print(letter, end='')
'''
for letter in input("Enter a word: "):
	if letter in 'aeiou':
		print(f'ub{letter}', end='')
	else:
		print(letter, end='')

'''
Exercise 2.5 In this exercise, you’ll explore this idea by writing a function, strsort, that takes a single string 
as its input, and returns a string. The returned string should contain the same characters as the input, except that 
its characters should be sorted in order, from smallest Unicode value to highest Unicode value.

For example, the result of invoking strsort('cba') will be the string abc.
'''


def strsort(s):
	return ''.join(sorted(s))

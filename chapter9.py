"""
Chapter 9
A chapter to learn about objects and object oriented programming.
"""


class ScoreList:
	def __init__(self, scores):
		self.scores = scores

	def average(self):
		return sum(self.scores) / len(self.scores)


scores = ScoreList([85, 95, 98, 87, 80, 92])
print(f'The final score is {scores.average()}.')

'''
Define a class, Scoop, that represents a single scoop of ice cream. Each scoop should have a single attribute, flavor,
a string that you can initialize when you create the instance of Scoop.
'''


class Scoop:
	def __init__(self, flavor):
		self.flavor = flavor


# Alternative way of creating scoops.
# scoops = [Scoop(flavor) for flavor in ('chocolate', 'vanilla', 'persimmon')]
def create_scoops():
	scoops = [Scoop('chocolate'), Scoop('vanilla'), Scoop('persimmon')]
	for scoop in scoops:
		print(scoop.flavor)


create_scoops()

'''
Create a Bowl class representing a bowl into which we can put our ice cream. No modification for Scoop class needed.
'''


class Bowl:
	max_scoops = 3

	def __init__(self):
		self.scoops = []

	def add_scoops(self, *new_scoops):
		for scoop in new_scoops:
			if len(self.scoops) < Bowl.max_scoops:
				self.scoops.append(scoop)

	def __repr__(self):
		return '\n'.join(s.flavor.title() for s in self.scoops)


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')
s4 = Scoop('flavor 4')
s5 = Scoop('flavor 5')

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
b.add_scoops(s4, s5)
print(b)

'''
Beyond the exercise assignment.
Create a Book class which will have a title, author and a price. Then, create a Shelf class which will contains books
and it should allow books to be added by a method called "add_book". Finally, implement "total_price" method which will 
total the prices of the books on the shelf.
'''


class ManyBooksOnShelfError(Exception):
	pass


class Book:
	def __init__(self, title, author, price, width):
		self.title = title
		self.author = author
		self.price = price
		self.width = width


class Shelf:
	def __init__(self, width):
		self.books = []
		self.width = width

	def add_book(self, *new_books):
		for book in new_books:
			if self.total_width() + book.width > self.width:
				raise ManyBooksOnShelfError('Too many books!')
			self.books.append(book)

	def total_price(self):
		return sum(book.price for book in self.books)

	def has_book(self, title):
		return title in (book.title for book in self.books)

	def total_width(self):
		return sum(book.width for book in self.books)

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
			if len(self.scoops) < self.max_scoops:
				self.scoops.append(scoop)

	def __repr__(self):
		return '\n'.join(s.flavor.title() for s in self.scoops)


class BigBowl(Bowl):
	max_scoops = 5


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')
s4 = Scoop('flavor 4')
s5 = Scoop('flavor 5')

bb = BigBowl()
bb.add_scoops(s1, s2)
bb.add_scoops(s3)
bb.add_scoops(s4, s5)
print(bb)

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


# Create a Person class with a class attribute that increases each time a new instance of the class is created.
class Person:
	population = 0

	def __init__(self):
		Person.population += 1

	def __del__(self):
		Person.population -= 1


p1 = Person()
p2 = Person()
p3 = Person()
p4 = Person()
p5 = Person()

print("Before triggering __del__: ", p1.population, ' ' * 5, Person.population)

del p1, p4

print("After triggering __del__: ", p2.population, ' ' * 5, Person.population)


class Transaction:
	balance = 0

	def __init__(self, amount):
		if amount < 0:
			Transaction.balance -= amount
		else:
			Transaction.balance += amount


class Envelope:
	postage_multiplier = 10

	def __init__(self, weight):
		self.weight = weight
		self.postage = 0
		self.was_sent = False

	def add_postage(self, amount):
		self.postage += amount

	def send(self):
		if self.postage >= self.weight * self.postage_multiplier:
			self.was_sent = True
		else:
			raise NotEnoughPostageError('You do not have enough postages')


class NotEnoughPostageError(Exception):
	pass


class BigEnvelope(Envelope):
	postage_multiplier = 15


class FlexibleDict(dict):
	def __getitem__(self, key):
		try:
			if key in self:
				pass
			elif str(key) in self:
				key = str(key)
			elif int(key) in self:
				key = int(key)
		except ValueError:
			pass

		return dict.__getitem__(self, key)


class StringKeyDict(dict):
	def __setitem__(self, key, value):
		dict.__setitem__(self, str(key), value)


fd = FlexibleDict()
fd['a'] = 100
print(fd['a'])

fd[5] = 500
print(fd[5])

fd[1] = 100
print(fd['1'])

fd['1'] = 100
print(fd[1])

string_dict = StringKeyDict()
string_dict[10] = 100
print(string_dict['10'])


class RecentDict(dict):
	def __init__(self, maxsize):
		super().__init__()
		self.maxsize = maxsize

	def __setitem__(self, key, value):
		dict.__setitem__(self, str(key), value)

		if len(self) > self.maxsize:
			self.pop(list(self.keys())[0])


class FlatList(list):
	def append(self, values):
		try:
			for value in values:
				list.append(value)
		except TypeError:
			list.append(self, values)


class Bread:
	def __init__(self):
		self.calories = 66
		self.carbs = 12
		self.sodium = 170
		self.sugar = 1
		self.fat = 0.8

	def get_nutrition(self, slices):
		return {key: value * slices for key, value in vars(self).items()}


class WholeWheatBread(Bread):
	def __init__(self):
		self.calories = 67
		self.carbs = 12
		self.sodium = 138
		self.sugar = 1.4
		self.fat = 1


class RyeBread(Bread):
	def __init__(self):
		self.calories = 67
		self.carbs = 12
		self.sodium = 172
		self.sugar = 1
		self.fat = 0.8


class Animal:
	def __init__(self, color, legs):
		self.species = self.__class__.__name__
		self.color = color
		self.legs = legs

	def __repr__(self):
		return f'{self.color.title()} {self.species}, {self.legs} legs'


class Wolf(Animal):
	def __init__(self, color):
		super().__init__(color, 4)


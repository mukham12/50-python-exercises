import os


class MyEnumerateIterator:
	def __init__(self, data, start):
		self.data = data
		self.index = start

	def __next__(self):
		if self.index >= len(self.data):
			raise StopIteration
		value = (self.index, self.data[self.index])
		self.index += 1
		return value


class MyEnumerate:
	"""Simple replacement for enumerate"""

	def __init__(self, data, start=0):
		self.data = data
		self.start = start

	def __iter__(self):
		return MyEnumerateIterator(self.data, self.start)


def my_enumerate(data, start=0):
	index = start

	for one_item in data:
		yield index, one_item
		index += 1


class CircleIterator:
	def __init__(self, data, max_times):
		self.data = data
		self.max_times = max_times
		self.index = 0

	def __next__(self):
		if self.index >= self.max_times:
			raise StopIteration

		iterated_data = getattr(self, self.returns)

		value = iterated_data[self.index % len(iterated_data)]
		self.index += 1
		return value

	def __iter__(self):
		return type(self)(self.data, self.max_times)


# A class that iterates over data and if the index ever is greater than data then it will return back and start from
# the beginning.
class Circle(CircleIterator):
	def __init__(self, data, max_times):
		super().__init__(data, max_times)
		self.returns = 'data'


def circle(data, max_times):
	for index in range(max_times):
		yield data[index % len(data)]


# A class that mimics the work of built-in function range which is an iterable and used extensively with for loops.
class MyRange:
	def __init__(self, first, second=None, step=1):
		if second is None:
			self.current = 0
			self.stop = first
		else:
			self.current = first
			self.stop = second
		self.step = step

	def __iter__(self):
		return self

	def __next__(self):
		if self.current >= self.stop:
			raise StopIteration

		value = self.current
		self.current += self.step
		return value


def all_lines(path):
	"""
	An iterator that returns, one at a time, each line from each file in a named directory.
	Any file that cannot be opened, for whatever reason, is ignored.
	"""

	for filename in os.listdir(path):
		full_filename = os.path.join(path, filename)
		try:
			for line in open(full_filename):
				yield line
		except OSError:
			pass

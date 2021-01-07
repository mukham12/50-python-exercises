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
	"""Iterator for Circle."""

	def __init__(self, data, max_times):
		self.data = data
		self.max_times = max_times
		self.index = 0

	def __next__(self):
		if self.index >= self.max_times:
			raise StopIteration
		value = self.data[self.index % len(self.data)]
		self.index += 1
		return value



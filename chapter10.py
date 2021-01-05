class MyEnumerate:
	"""Simple replacement for enumerate"""

	def __init__(self, data):
		self.data = data
		self.index = 0

	def __iter__(self):
		return self

	def __next__(self) -> tuple:
		if self.index >= len(self.data):
			raise StopIteration
		self.index += 1
		return self.index, self.data[self.index]
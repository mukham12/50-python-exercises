import os
import time
import pytest


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


# def all_lines(path):
# 	"""
# 	An iterator that returns, one at a time, each line from each file in a named directory.
# 	Any file that cannot be opened, for whatever reason, is ignored.
# 	"""
#
# 	for filename in os.listdir(path):
# 		full_filename = os.path.join(path, filename)
# 		try:
# 			for line in open(full_filename):
# 				yield line
# 		except OSError:
# 			pass


def all_lines_tuple(path):
	for file_index, filename in enumerate(os.listdir(path)):
		full_filename = os.path.join(path, filename)
		try:
			for line_index, line in enumerate(open(full_filename)):
				yield full_filename, file_index, line_index, line
		except OSError:
			pass


def open_file_safely(filename):
	try:
		return open(filename)
	except OSError:
		return None


def all_lines_alt(path):
	all_files = [open_file_safely(os.path.join(path, filename)) for filename in os.listdir(path)]

	while all_files:
		for one_file in all_files:
			if one_file is None:
				all_files.remove(one_file)
				continue

			one_line = one_file.readline()

			if one_line:
				yield one_line
			else:
				all_files.remove(one_file)


def all_lines(path, s):
	for filename in os.listdir(path):
		full_filename = os.path.join(path, filename)
		try:
			for line in open(full_filename):
				if s in line:
					yield line
		except OSError:
			pass


def elapsed_since(data):
	"""
	A generator that takes an iterable as input. With each iteration, it yields a tuple containing the
	data and the time since the previous iteration.
	"""

	last_time = None
	for item in data:
		current_time = time.perf_counter()
		delta = current_time - (last_time or current_time)
		last_time = time.perf_counter()
		yield delta, item


def elapsed_since(data, min_wait):
	last_time = None
	for item in data:
		current_time = time.perf_counter()
		delta = current_time - (last_time or current_time)

		if delta < min_wait:
			time.sleep(min_wait - delta)

		last_time = time.perf_counter()
		yield delta, item


def file_usage_timing(dirname):
	for one_filename in os.listdir(dirname):
		full_filename = os.path.join(dirname, one_filename)

		yield full_filename, os.stat(full_filename).st_mtime, os.stat(full_filename).st_ctime, os.stat(
				full_filename).st_atime


def yield_filter(data, func):
	for one_item in data:
		if func(one_item):
			yield one_item


def mychain(*args):
	"""
	Generator that takes any number of iterables as arguments. It yields, one at a time, each of the
	elements of each iterable. It is similar to itertools.chain.
	"""

	for arg in args:
		for item in arg:
			yield item


def all_lines(p):
	return mychain(*(open(os.path.join(p, file)) for file in os.listdir(p) if os.path.isfile(os.path.join(p, file))))


def myzip(*args):
	for i in range(len(min(args, key=len))):
		yield tuple(arg[i] for arg in args)


def myrange(first, second=None, step=1):
	if second is None:
		current = 0
		stop = first

	else:
		current = first
		stop = second

	while current < stop:
		yield current
		current += step


def test_simple():
	m = MyEnumerate('abc')
	assert list(m) == [(0, 'a'), (1, 'b'), (2, 'c')]


def test_is_iterable():
	m = MyEnumerate('abc')
	assert hasattr(m, '__iter__')


@pytest.mark.parametrize('iterable, maxtimes, output', [
	('abcd', 7, 'abcdabc'),
	([10, 20, 30], 2, [10, 20]),
	([10, 20, 30], 8, [10, 20, 30, 10, 20, 30, 10, 20]),
	])
def test_circle(iterable, maxtimes, output):
	assert list(Circle(iterable, maxtimes)) == list(output)


@pytest.fixture
def small_file(tmp_path):
	f = tmp_path / 'smallfile.txt'
	f.write_text('''This is the first line
and this is the second line
and this is, to no one's surprise, the third line
but the biggest word will probably be encyclopedia''')
	return f


@pytest.fixture
def big_file(tmp_path):
	f = tmp_path / 'bigfile.txt'
	f.write_text('''This is the first line of a big file

and this is the second line
and this is, to no one's surprise, the third line
but the biggest word will probably be encyclopedia''')
	return f


def test_iterator(tmp_path):
	g = all_lines(tmp_path)
	assert iter(g) == g


def test_empty(tmp_path):
	lines = list(all_lines(tmp_path))
	assert len(lines) == 0


def test_simple(tmp_path, small_file, big_file):
	lines = list(all_lines(tmp_path))
	assert len(lines) == 9
	assert lines[0] == 'This is the first line\n'
	assert lines[-1] == 'but the biggest word will probably be encyclopedia'


def test_simple():
	for index, t in enumerate(elapsed_since('abc')):
		assert isinstance(t, tuple)
		assert isinstance(t[0], float)
		assert isinstance(t[1], str)

		if index == 0:
			assert t[0] == 0

		else:
			assert int(t[0]) == 1

		time.sleep(1)


def test_empty():
	assert list(mychain()) == []


def test_some():
	assert list(mychain('abc', [10, 20, 30])) == ['a', 'b', 'c', 10, 20, 30]

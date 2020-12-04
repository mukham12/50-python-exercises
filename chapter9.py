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

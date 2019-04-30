class Player:
	def __init__(self, name, intelligence):
		self.name = name
		self.intelligence = intelligence
		self.score = 0
		self.hasPlayed = []

	def victory(self):
		self.score += 3

	def draw(self):
		self.score += 1



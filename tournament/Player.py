class Player:
	def __init__(self, name, intelligence):
		self.name = name
		self.intelligence = intelligence
		self.score = 0
		self.hasPlayed = []

	def victoire(self):
		self.score += 3

	def egalite(self):
		self.score += 1



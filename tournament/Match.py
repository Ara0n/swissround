class Match:
	def __init__(self, p1, p2, bo, Game):
		self.p1 = p1
		self.p2 = p2
		self.bo = bo
		self.Game = Game(self.p1, self.p2)
		self.results = {"p1": 0, "pat": 0, "p2": 0}

	def play(self):
		if self.p1.name == "bye":
			self.p2.victory()

		elif self.p2.name == "bye":
			self.p1.victory()

		else:
			while self.results["p1"] < self.bo//2+1 and self.results["pat"] < self.bo//2+1 and self.results["p2"] < self.bo//2+1 and (self.results["p1"]+self.results["pat"]+self.results["p2"]) < self.bo:
				self.Game.play()

				if self.Game.results == 1:
					self.results["p1"] += 1
				elif self.Game.results == 2:
					self.results["p2"] += 1
				else:
					self.results["pat"] += 1

			self.p1.hasPlayed.append(self.p2)
			self.p2.hasPlayed.append(self.p1)

			if self.results["p1"] > self.results["p2"] and self.results["p1"] > self.results["pat"]:
				self.p1.victory()
			elif self.results["p2"] > self.results["p1"] and self.results["p2"] > self.results["pat"]:
				self.p2.victory()
			else:
				self.p1.draw()
				self.p2.draw()

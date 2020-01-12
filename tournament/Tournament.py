from math import ceil, log2
from .Player import Player
from .Match import Match



def merge(a, b):
	c = []

	pa = 0
	pb = 0

	la = len(a)
	lb = len(b)

	while pa < la and pb < lb:
		player1 = a[pa]
		player2 = b[pb]

		if player1.score > player2.score:
			c.append(player1)
			pa += 1
		else:
			c.append(player2)
			pb += 1

	for i in range(pa, la):
		c.append(a[i])

	for i in range(pb, lb):
		c.append(b[i])

	return c


def mergeSort(a):
	l = len(a)
	d = l // 2

	if l <= 1:
		r = a
	else:
		r = merge(mergeSort(a[0:d]), mergeSort(a[d:l]))

	return r


class Tournament:
	def __init__(self, playerList, Game, bo):
		self.ranking = playerList
		self.nbPlayer = len(playerList)
		self.nbRounds = ceil(log2(self.nbPlayer))
		self.roundsPlayed = 0
		self.winner = None
		self.Game = Game
		self.bo = bo
		self.round = []

		if self.nbPlayer%2 == 1:
			self.ranking.append(Player("Bye", None))

	def createRound(self):
		self.round.clear()
		tempMM = self.ranking.copy()

		while len(tempMM) > 0:
			opponent = 1
			while (tempMM[opponent] in tempMM[0].hasPlayed) and opponent < len(tempMM):
				opponent += 1
			if opponent == len(tempMM):
				opponent = 1

			self.round.append(Match(tempMM[0], tempMM[opponent], self.bo, self.Game))
			tempMM.pop(opponent)
			tempMM.pop(0)

	def playRound(self):
		for match in self.round:
			match.play()
		self.roundsPlayed += 1

	def updateRank(self):
		self.ranking = mergeSort(self.ranking)

		# the Bye must be the last player
		for i in range(len(self.ranking)-1):
			if self.ranking[i].name == "Bye":
				temp = self.ranking[i]
				self.ranking[i] = self.ranking[i+1]
				self.ranking[i+1] = temp

def infoSwiss(nbJ):
	nbRounds = ceil(log2(nbJ))
	nbMpR = floor(nbJ/2)
	nbMatchs = nbRounds * nbMpR
	print("nb rounds: {0}\nnb matchs per round: {1}\nnb matchs of the tournament {2}".format(nbRounds, nbMpR, nbMatchs))

import random

def pickRandomCard(numOfCards = 5):
	deck = ["2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC",
	    "QC", "KC", "AC", "2D", "3D", "4D", "5D", "6D", "7D", "8D",
	    "9D", "10D", "JD", "QD", "KD", "AD", "2H", "3H", "4H", "5H",
	    "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AH", "2S",
	    "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS",
	    "KS", "AS"]
	#print(random.choice(deck))
	cards = []
	# for i in range(numOfCards):
	# 	cards.append(random.choice(deck))

	#NOTE the potential for duplicates using choice

	#the objective of the above block can be achieved using random's sample method
	#sample makes sure that those cards that have been picked will not be picked again
	cards = random.sample(deck, k=numOfCards)
	print("Your hand:")
	print(cards)

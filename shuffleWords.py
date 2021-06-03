import random
words = ['rabbit', 'horse', 'goat', 'bear', 'chicken']
list_words = [list(w) for w in words]

for w in list_words:
	random.shuffle(w)
scrambled_words = [''.join(w) for w in list_words]

for w in scrambled_words:
	print(w)
import secrets
#secrets is more secure than random (computationally secure)

def passWordGenerator(nr_letters=5, nr_numbers=3, nr_symbols=4):
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	print("Welcome to the PyPassword Generator!")
	# nr_letters= int(input("How many letters would you like in your password?\n")) 
	# nr_symbols = int(input(f"How many symbols would you like?\n"))
	# nr_numbers = int(input(f"How many numbers would you like?\n"))

	totalLength = nr_numbers + nr_letters + nr_symbols

	randomLetters = []
	for i in range(0, nr_letters):
		randomChoice = secrets.choice(letters)
		randomLetters.append(randomChoice)
	del letters

	randomNumbers = []
	for i in range(0, nr_numbers):
		randomChoice = secrets.choice(numbers)
		randomNumbers.append(randomChoice)
	del numbers

	randomSymbols = []
	for i in range(0, nr_symbols):
		randomChoice = secrets.choice(symbols)
		randomSymbols.append(randomChoice)
	del symbols
	del randomChoice


	category = ["letters", "numbers", "symbols"]
	genDict = {"letters": randomLetters, "numbers": randomNumbers, "symbols": randomSymbols}
	#print(genDict)

	del randomLetters
	del randomNumbers
	del randomSymbols

	newPassWordList = []
	currentCategory = secrets.choice(category)

	while len(newPassWordList) <= totalLength or category:
		if not genDict[currentCategory]:
			del genDict[currentCategory]
			category.remove(currentCategory)
			#print(category)
			if not category:
				break
			currentCategory =  secrets.choice(category)
			continue
		lastRandomCharIdx = len(genDict[currentCategory]) - 1
		newPassWordList.append(genDict[currentCategory][lastRandomCharIdx])
		genDict[currentCategory].pop()
		currentCategory =  secrets.choice(category)
		#print(newPassWordList)

	#del category

	newPassWord = "".join(newPassWordList)

	print(f"Your new password is {newPassWord}")

	#random.choice and random.shuffle are also useful methods

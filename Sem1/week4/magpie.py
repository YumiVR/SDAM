import sys
print ("welcome to the program")
print ("press enter to exit the program")

song = {
	1 : "One for Sorrow",
	2 : "Two for Joy",
	3 : "Three for a Girl",
	4 : "Four for a Boy",
	5 : "Five for Silver",
	6 : "Six for Gold",
	7 : "Seven for a secret never to be to"
}

while True:
	try:
		print(song[int(input("Enter a number: "))])
	except:
		print("Not a permited number")
		print("would you like to exit?")
		userinput = input("(y) for Yes or (n) for No > ")
		if userinput == 'y':
			sys.exit()
		elif userinput == 'n':
			print("No Exit")

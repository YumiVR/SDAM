#import lib's
import sys
import random
import time 

line = "-----------------------------------------------------------------"

#-------------------------------------------------------------------------------------


old_card = "nul"
old_suit = "nul"

#-------------------------------------------------------------------------------------

cardnum = random.randint(1, 13) #generate random card number 1 to 13
cardsuitnum = random.randint(1, 4) #generate what suit it will be 

#-------------------------------------------------------------------------------------

print ("Welcome to High_Low.py")
time.sleep(1)

while True: #this while loop lets the program re-run till the user chooses to quit. 
	
	cardnum = random.randint(1, 13)
	cardsuitnum = random.randint(1, 4)
	
#-------------------------------------------------------------------------------------

#Setting the Random Numbers to the Suit's

	try:
		if cardsuitnum == 1:
			cardsuit = "of Diamonds"
		elif cardsuitnum == 2:
			cardsuit = "of Spades"
		elif cardsuitnum == 3:
			cardsuit = "of Clubs"
		elif cardsuitnum == 4:
			cardsuit = "of Hearts"

#-------------------------------------------------------------------------------------

#Displaying the Random Numbers to the Name's of the cards and adding the Suit

		if cardnum == 1:
			print ("Your Card is Ace", cardsuit)
		elif cardnum == 11:
			print ("Your card is Jack", cardsuit)
		elif cardnum == 12:
			print ("Your card is Queen", cardsuit)
		elif cardnum == 13:
			print ("Your card is King", cardsuit)
		else:
			print ("Your card is",cardnum, cardsuit)
		
#-------------------------------------------------------------------------------------

#Displaying a menu for the user to choose their next action

			print ("Guess higher or lower, or new card?")
			menu = input("(t) for try and guess (n) for new card (x) to exit >")

#if the user inpus "n" the program will generate a new card

		if menu == ("n"):
			print ()
		
# if the user inputs "x" the program will exit 

		elif menu == ("x"):
			print ("Thankyou for using High_Low.py")
			time.sleep(1)
			print ("Shutting Down Safely!")
			break

#-------------------------------------------------------------------------------------

#if the user inputs "t" the program will start the sequance of setting up variables for the guess


		elif menu == ("t"):
			old_card = cardnum #storing the old card to memory 
			old_suit = cardsuit # storing the old Suit to memory

#Generating new cards

			cardnum = random.randint(1, 13)
			cardsuitnum = random.randint(1, 4)

#creating a menu that is apeeling to the user

			print ("")
			print ("          Card Number        ")
			print ("           1 = Higher        ")
			print ("           2 = Lower         ")
			print ("")
				

			user_guess = int(input("Higher or Lower? >")) #asking the user fot their guess 
			
#working out if higher or lower
	
			if user_guess == 1: #checking if the users input was 1
				user_guess = cardnum + 1 #changing the users guess to the old card + 1

			elif user_guess == 2: #checking if the users input was 2
				user_guess = cardnum - 1 #changing the users guess to the old card - 1

			if user_guess > cardnum: #comparison for win
				print ("Congratulations, You Win! ") 
			elif user_guess < cardnum:
				print ("Sorry, You Loose! ") #comparison for loose
			print ("The card was the", cardnum, cardsuit)
			time.sleep(1)
			print (line)


#-------------------------------------------------------------------------------------

#error message 
	except:
		print ("Error Detected, Shutting Down!")

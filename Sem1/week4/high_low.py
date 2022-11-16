#import lib's
import sys
import random
import time 

#valid is a variable that we have to let the program loop till the user chooses to exit.
valid = "false"

#-------------------------------------------------------------------------------------


old_card = "nul"
old_suit = "nul"

#-------------------------------------------------------------------------------------

cardnum = random.randint(1, 13) #generate random card number 1 to 13
cardsuitnum = random.randint(1, 4) #generate what suit it will be 

#-------------------------------------------------------------------------------------

print ("Welcome to High_Low.py")
time.sleep(1)

while valid == "false": #this while loop lets the program re-run till the user chooses to quit. 
	
	cardnum = random.randint(1, 13)
	cardsuitnum = random.randint(1, 4)
	
#-------------------------------------------------------------------------------------

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
		print ("Guess higher or lower, or new card?")
		menu = input("(t) for try and guess (n) for new card (x) to exit >")

#-------------------------------------------------------------------------------------

		if menu == ("n"):
			print ()
		
		elif menu == ("x"):
			print ("Shutting Down Safely!")
			print ("Thankyou for using High_Low.py")
			break

#-------------------------------------------------------------------------------------

		elif menu == ("t"):
			old_card = cardnum 
			old_suit = cardsuit

			cardnum = random.randint(1, 13)
			cardsuitnum = random.randint(1, 4)

			print ("")
			print ("          Card Number        ")
			print ("            1 = Ace          ")
			print (" 2 = 10 are the card numbers ")
			print ("           11 = Jack         ")
			print ("           12 = Queen        ")
			print ("           13 = King         ")
			print ("")

			print ("            Card Suit        ")
			print ("          1 = Diamonds       ")
			print ("          2 = Spades         ")
			print ("          3 = Clubs          ")
			print ("          4 = Hearts         ")
			print ("")
				

			user_guess1 = int(input("Guess the new card nuber? >"))
			user_guess2 = int(input("Guess the new card suit? >"))

			if user_guess1 == old_card & user_guess2 == old_suit:
				print ("Congragts you win")
			else:
				print ("You loose")


#-------------------------------------------------------------------------------------

	except:
		print ("Error Detected, Shutting Down!")
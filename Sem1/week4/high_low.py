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

#Defining 

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
			print ("           1 = Higher        ")
			print ("           2 = Lower         ")
			print ("")
				

			user_guess = int(input("Higher or Lower? >"))
			
			if user_guess == 1:
				user_guess = cardnum + 1
			elif user_guess == 2:
				user_guess = cardnum - 1

			if user_guess > cardnum:
				print ("Congratulations, You Win! ")
			elif user_guess < cardnum:
				print ("Sorry, You Loose! ")


#-------------------------------------------------------------------------------------

	except:
		print ("Error Detected, Shutting Down!")
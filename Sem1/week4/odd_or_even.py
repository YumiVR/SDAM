import sys
program_valid = False
line = "--------------------------------------"
while not program_valid:

	try:
		print (line)
		print ("1) Use Program")
		print ("2) Exit Program")
		usermenu = int(input("Enter a option: "))

		if usermenu == 1:

			valid = False

			while not valid:
				try:
					print (line)
					UserInterger = int(input("Input a Number please: "))
					valid = False

					print (line)
					valid = True
					if (UserInterger % 2) == 0:
						print ("The number is even")
					else:
						print ("The provided number is odd")
				except:
					print (line)
					print ("Invalid input, Try again")


		elif usermenu == 2:
			program_valid = True
			print (line)
			break

	except:
		print (line)
		print ("Invalid input, Try again ")


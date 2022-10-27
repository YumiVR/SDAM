import sys
program_valid = "false"
while program_valid == "false":

	try:
		print ("--------------------------------------")
		print ("1) Use Program")
		print ("2) Exit Program")
		usermenu = int(input("Enter a option: "))

		if usermenu == 1:

			valid = "false"

			while valid == "false":
				try:
					print ("--------------------------------------")
					UserInterger = int(input("Input a Number please: "))
					valid = "false"

					if (UserInterger % 2) == 0:
						print ("--------------------------------------")
						print ("The number is even")
						valid = "true"
					else:
						print ("--------------------------------------")
						print ("The provided number is odd")
						valid = "true"
				except:
					print ("--------------------------------------")
					print ("Invalid input, Try again")


		elif usermenu == 2:
			program_valid = "true"
			print ("--------------------------------------")
			break

	except:
		print ("--------------------------------------")
		print ("Invalid input, Try again ")


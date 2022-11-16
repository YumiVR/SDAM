import sys
program_valid = "false"
line = "--------------------------------------"
while program_valid == "false":

	try:
		print (line)
		print ("1) Use Program")
		print ("2) Exit Program")
		usermenu = int(input("Enter a option: "))

		if usermenu == 1:

			valid = "false"

			while valid == "false":
				try:
					print (line)
					UserInterger = int(input("Input a Number please: "))
					valid = "false"

					if (UserInterger % 2) == 0:
						print (line)
						print ("The number is even")
						valid = "true"
					else:
						print (line)
						print ("The provided number is odd")
						valid = "true"
				except:
					print (line)
					print ("Invalid input, Try again")


		elif usermenu == 2:
			program_valid = "true"
			print (line)
			break

	except:
		print (line)
		print ("Invalid input, Try again ")


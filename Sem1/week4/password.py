
# Password Entry

valid = False

while not valid:
	try:
		passwd_stored = str(input("Enter a new password: "))
		valid = True
	
	except:
		print("Invalid In put, Try again!")

# Password Checking

passcheck = False

while not passcheck:
	try:
		passwd_entered = input("Please input your password: ")
		
		if passwd_entered == passwd_stored:
			print ("Welcome User")
			passcheck = True

		else:
			print ("Wrong password, Try Again!")	

	except:
		print("Please Try Again!")

 

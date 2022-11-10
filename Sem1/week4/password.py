
# Password Entry

valid = "false"

while valid == "false":
	try:
		passwd_stored = str(input("Enter a new password: "))
		valid = "true"
	
	except:
		print("Invalid In put, Try again!")

# Password Checking

passcheck = "false"

while passcheck == "false":
	try:
		passwd_entered = input("Please input your password: ")
		
		if passwd_entered == passwd_stored:
			print ("Welcome User")
			passcheck = "true"

		else:
			print ("Wrong password, Try Again!")	

	except:
		print("Please Try Again!")

 
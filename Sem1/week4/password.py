
valid = "false"

passwd = "rocket"

while valid == "false":
	try:
		passwd_entered = input("Please input your password: ")
		
		if passwd_entered == passwd:
			print ("Welcome User")
			valid = "true"
			

		else:
			print ("Wrong password, Try Again!")	

	except:
		print("Please Try Again!")


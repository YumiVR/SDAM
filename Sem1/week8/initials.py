import sys

print ("Type 'help' for a list of commands")


while True:
	try:
		usermenu = input(">")

		if usermenu == 'help':
			print("")
			print("help 	- print this menu")
			print("exit 	- quit the program")
			print("initial - use the initial app")
			print("")
		
		elif usermenu == 'exit':
			break

		elif usermenu == 'initial':
			print("")
			fn = input("what is yout Full Name? >").split()

			for inital in fn:
				print(inital[0], inital[])	
				print("")
				break
	except:
		print("try again!")

sys.exit()

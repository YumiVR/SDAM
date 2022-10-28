import sys
import math
program_validity = "false"

while program_validity ==  "false":
	try:
		UserMbpsInput =  int(input("Input Bandwith limit in Mbps: "))
		UsersRequired = int(input("Input Users Required: "))
		break

	except:
		print ("Unexpected error, Try Again!")

Userbps = UserMbpsInput * 1000000
print ("Your Bandwith in bps is", Userbps)

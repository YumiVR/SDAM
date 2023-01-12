import sys
import math

while True:
	try:
		UserMbpsInput =  int(input("Input Bandwith limit in Mbps: "))
		UsersRequired = int(input("Input Users Required: "))
		break

	except:
		print ("Unexpected error, Try Again!")

Userbps = UserMbpsInput * 1000000
print ("Your Bandwith in bps is", Userbps)

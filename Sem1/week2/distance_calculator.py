import math
valid = "false"


while valid == "false":
	try:
		intvelo = int(input("Input Initial Velocity: "))
		timetaken = int(input("Input Time Taken: "))
		accel = int(input("Input Acceleration: "))
		valid = "true"
	except:
		print ("An unexpected error occured, please try again. ")


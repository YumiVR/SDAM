import math

#error handeling
valid = False

#getting users inputs
while not valid:
	try:
		intvelo = int(input("Input Initial Velocity: "))
		timetaken = int(input("Input Time Taken: "))
		accel = int(input("Input Acceleration: "))

		#setting valid to true to breake from the while
		valid = True
	except:
		print ("An unexpected error occured, please try again. ")

#calculating the equasion
ut = intvelo * timetaken
halfatsq = 0.5 * accel * timetaken**2
distance = ut + halfatsq

#output answer to user
print ("distance is", distance)


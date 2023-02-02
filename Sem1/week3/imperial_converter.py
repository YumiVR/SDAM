#error handeling
valid = False
while not valid:
	try:
		feet = int(input("Input height in Feet: "))
		inches = int(input("Input height in Inches: "))
		valid = True


	except:
		print ("Try Again")

#cm conversion

cm1 = feet * 12
cm2 = cm1 + inches
cm = cm2 * 2.54

#calculation for diffrent converions.
km = cm / 100000
print ("Height in Kilometers: ",km)

m = cm / 100
print ("Height in Meteres: ",m)

#cm print
print ("Height in Centimeteres: ",cm)

mm = cm * 10
print ("Height in Milimeteres: ",mm)

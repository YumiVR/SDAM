#define varibles
valid = "false"
callrate = 0.15
vat=0.2

#asking user how long the call was with error handeling
while valid == "false":
	try:
		time_mins = int(input("How long was the call: "))
		valid = "true"
	except:
		print ("An unexpected error occurred")

#calculating price of call without vat
calltimeprice = callrate * time_mins

#calculating vat
totalvat = calltimeprice * vat

#calculating total price with vat
totbill = calltimeprice + totalvat

#outputting to user
print ("Number of Minutes used", time_mins)
print ("Basic call charge: £",calltimeprice)
print ("VAT due: £",totalvat)
print ("Total bill: £",totbill)

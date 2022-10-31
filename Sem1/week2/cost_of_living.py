# Asking the user to input their costs of things
rent =  float(input("Input Rent Cost: "))
gas = float(input("Input Gas Cost: "))
electric = float(input("Input Electricity: "))
water = float(input("Input Water: "))
ctax = float(input("Input Council Tax: "))

# Caculating the Sum
total = rent + gas + electric + water + ctax

# Printing the Output
print ("Your monthly expences are:")
print ("Rent:         £", rent)
print ("Gas:          £", gas)
print ("Electricity:  £", electric)
print ("Water:        £", water)
print ("Council Tax:  £", ctax)
print ("=================================")
print ("Total:        £", round(total,2))
print ("=================================")
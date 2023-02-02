#Ask the user for the amount and price of Peaches
peaches_count = int(input("Peaches - how many? "))
peaches_price = float(input("Peaches - price? "))


#Ask the user for the amount and price of Beans
beans_count = int(input("Beans - how many? "))
beans_price = float(input("Beans - price? "))


#Ask the user for the amount and price of Chicken
chicken_count = int(input("Chicken pieces - how many? "))
chicken_price = float(input("Chicken pieces - price? "))


#Ask the user for the amount and price of Socks
socks_count = int(input("Socks - how many? "))
socks_price = float(input("Socks - price? "))


#Ask the user for the amount and price of Water
water_count = int(input("Bottle of water - how many? "))
water_price = float(input("Bottle of water - price? "))

#Working out the total
total_cost = (peaches_count * peaches_price) + (beans_count * beans_price) + (chicken_count * chicken_price) + (socks_count * socks_price) + (water_count * water_price)
total_items = peaches_count + beans_count + chicken_count + socks_count + water_count

#printing the answert in a readable format 
print("Total number of items purchased: " + str(total_items))
print("Your weekly shop cost: $" + str(total_cost))

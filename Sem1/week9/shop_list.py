print ("welcome to shop_list.py")
print ("type :q to quit")
item = []
itemprice = []

while True:
	print("")
	data = input("Enter Item >")
	if data == ':q':
		break

	data2 = int(input("Enter Price >"))
	
	itwappend(data)
	itemprice.append(data2)

for items in item:
	print("")
	print ("you said", items)
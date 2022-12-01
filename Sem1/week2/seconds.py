
valid = 'false'
while valid == 'false':
	try:
		userseconds = int(input("Input amount of positive secconds: "))
		valid = 'true'
		
	except:
		print ("Invalid input, Try again please! ")

hours = userseconds // 3600
hourrem = userseconds % 3600
minutes =  hourrem // 60
seconds = hourrem % 60

print(tabulate([[userseconds]], headers=['Input']), tabulate([[hours]], headers=['Hours']), tabulate([[minutes]], headers=['Minutes']), tabulate([[seconds]], headers=['seconds']))
valid = 'true'

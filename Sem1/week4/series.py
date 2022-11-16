import sys

program_valid = "false"
valid =  "false"

while program_valid == "false":
while valid == "false":
	try:
		sumpos = 0
		sumneg = 0

		usernum1 = int(input("Enter First Number: "))
		usernum2 = int(input("Enter First Number: "))
		usernum3 = int(input("Enter First Number: "))
		usernum4 = int(input("Enter First Number: "))
		usernum5 = int(input("Enter First Number: "))
		valid = "true"
	except:
		print ("Invalid input, Try Again Please! ")

if usernum1 < 0:
	sumneg = sumneg + usernum1
else:
	sumpos	= sumpos + usernum1


if usernum2 < 0:
	sumneg = sumneg + usernum2
else:
	sumpos = sumpos + usernum2


if usernum3 < 0:
	sumneg = sumneg + usernum3
else:
	sumpos = sumpos + usernum3


if usernum4 < 0:
	sumneg = sumneg + usernum4
else:
	sumpos = sumpos + usernum4


if usernum5 < 0:
	sumneg = sumneg + usernum5
else:
	sumpos = sumpos + usernum5


print ("Sum of Negative Intergers >", sumneg)
print ("Sum of Positive Intergers >", sumpos)
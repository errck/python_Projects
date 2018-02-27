prompt = "Enter your age yo see the price of the ticket"
prompt += "\n type 'quit' to quit"
while True:
	age = input(prompt)
	if age == 'quit':
		break
	else:
		age = int(age)
		if age < 3:
			print("The ticket will be free")
		elif age >= 3 and age <=12:
			print("the ticket is $10")
		else:
			print("The ticket is $15")
			


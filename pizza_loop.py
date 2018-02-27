prompt = "What toppings would you like on your pizza?"
prompt += "\n type 'quit' to quit "
while True:
	toppings = input(prompt)
	if toppings == 'quit':
		break
	else:
		print("Okay, well add " + toppings + " to your pizza")


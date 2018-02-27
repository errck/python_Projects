prompt = "What toppings would you like on your pizza?"
prompt += "\n type 'quit' to quit "

active = True

while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	else:
		print(message)
	

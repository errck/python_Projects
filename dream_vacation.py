#reponses will be stored in dictionary
responses={}

while True:
	#ask questions
	name = input("What is your name? ")
	place=input("Where would you go for a dream vacation? ")
	#store the responses in dictionary
	responses[name] = place
	#ask to keep going or to stop
	repeat = input("Would anyone else like to respond? (Y/N)")
	if repeat == "N" or repeat == "n":
		break
			
#show the results
for name, place in responses.items():
	print(name.title() + "would like to go to :" + place.title())

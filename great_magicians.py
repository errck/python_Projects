def show_magicians(magis):
	for magi in magis:
		print(magi)

def make_great(magis):
	great_magicians=[]
	
	while magis:
		magician = magis.pop()
		great_magician = magician + ' The great'
		great_magicians.append(great_magician)
	
	for great_magician in great_magicians:
		magis.append(great_magicians)
		return magis
	

magicians=['Huodini','Blaine','Cris']
show_magicians(magicians)

print("\nThe great magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print("\n the orginal list ")
show_magicians(magicians)

favorite_places={'jen':['wal-mart','wal-greens','the gas station']
				,'kenneth':['KFC','library','the garage']
				,'mike':['his room','arcade','the closet']}
for name, places in favorite_places.items():
	print("\n" + name.title() + "'s favorite places are:")
	for place in places:
		print("\t" + place.title())
	

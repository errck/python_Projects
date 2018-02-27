louis={'type':'pug dog','owner':'Erick'}
goodboi={'type':'doberman dog','owner':'Moi'}
polly={'type':'parrot','owner':'Jim'}
pets=[louis,goodboi,polly]
counter=0
for pet in pets:
	counter= counter +1
	print("Pet "+ str(counter)+' ' +pet['type']+ " "+
	"owner " +pet['owner'])
	

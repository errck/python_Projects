def make_album(name, title, tracks=''):
	album= {'artist': name, 'album name': title}
	if tracks:
		album['tracks']= tracks
	return album


print("Enter 'quit at any time to stop the program.")

while True:
	title= input("Enter an album.")
	if title == "quit":
		break
	artist= input("enter an artist")
	if artist == "quit":
		break
	album = make_album(artist, title)
	print(album)
	


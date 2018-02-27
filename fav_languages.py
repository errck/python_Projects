fav_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python'}
poll_list=['ben','bob','jen','billy','phil']
for name in poll_list:
	if name in fav_languages.keys():
		print(name + " Thank you for taking the poll")
	else:
		print(name + " You should take the poll")
		



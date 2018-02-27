cities={'hong kong':{
			'country':'China',
			'population':'1456987',
			'fact':'its big'},
		'LA':{
			'country':'US',
			'population':'2456987',
			'fact':'it has a lot of pollution'},
		'Mexico city':{
			'country':'Mexico',
			'population':'5782987',
			'fact':'its sinking'},
			}
for city , cit_info in cities.items():
	print("\nCity: " + city)
	print("country: " + cit_info['country'])
	print("population: " + cit_info['population'])
	print("fact: " + cit_info['fact'])

favorite_nums = {
    'bert': ['4', '32'],
    'sarah': ['2','56'],
    'john':['12', '11'],
    'trey': ['43', '9'],
    'sena':['6','7']}
for name, numbers in favorite_nums.items():
	print("\n" + name.title() + "'s numbers are:")
	for nums in numbers:
		print("\t" + nums.title())



favorite_languages = {
    'jen': ['python', 'ruby','C#'],
    'sarah': ['c','cobalt'],
    'edward': ['ruby', 'go',],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
	for language in languages:
		print("" + language.title())

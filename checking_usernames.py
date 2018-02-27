current_users=["dude1","mike23","gg2","vegan1","strwr"]
new_users=["benner","mike23","ger3","ben2","skippy"]
for n_users in new_users:
	if n_users in current_users:
		print("Username is taken")
	else:
		print("The username is available")


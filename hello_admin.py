usernames=[]
if usernames:
	for users in usernames:
		if users=="admin":
			print("Hello Admin, would you like to see the new report?")
		else:
			print("hello "+ users)
else:
	print("there are no users")

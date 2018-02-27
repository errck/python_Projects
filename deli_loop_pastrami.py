print("the deli has ran out of pastrami")
sandwhich_orders=['hoagie','pastrami','italian','pastrami','cuaban',
					'pastrami','torta']
finished_sandwhiches=[]
while 'pastrami' in sandwhich_orders:
	sandwhich_orders.remove('pastrami')
#this while will print and put each sanwhich into finsihed list
while sandwhich_orders:
	sandwhich_being_made = sandwhich_orders.pop()
	print("I made your " + sandwhich_being_made + " sandwhich") 
	finished_sandwhiches.append(sandwhich_being_made)
#this loop will display the finiished sandwhiches loop
for item in finished_sandwhiches:
	print(item)

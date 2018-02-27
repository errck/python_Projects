person1={'fname':'jose','lname':'Sanchez','age':'21','city':'LA'}
person2={'fname':'Bert','lname':'renolds','age':'19','city':'NY'}
person3={'fname':'julie','lname':'greene','age':'23','city':'Baton \
 rouge'}
people=[person1,person2,person3]
for person in people:
	print(person['fname']+ " " +person['lname']
	+" "+person['age']+" "+person['fname'])

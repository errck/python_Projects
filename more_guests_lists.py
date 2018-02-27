guests=['Albert Einstein','Elon Musk','Steve Jobs']
print("Hello, " +guests[0]+ " you are invited to my dinner at 5pm")
print("Hello, " +guests[1]+ " you are invited to my dinner at 5pm")
print("Hello, " +guests[2]+ " you are invited to my dinner at 5pm")
print(guests[1] + " Cant make it")
guests[1]= "Alan Turing"
print("Hello, " +guests[0]+ " you are invited to my dinner at 5pm")
print("Hello, " +guests[1]+ " you are invited to my dinner at 5pm")
print("Hello, " +guests[2]+ " you are invited to my dinner at 5pm")
print("Bigger table found, more people coming")
guests.insert(0,"Elvis Presley")
guests.insert(2,"Kurt Cobain")
guests.append("John F. Kennedy")
print("Hello, " +guests[0]+ " you are invited to my dinner at 5pm")
print("Hello, " +guests[1]+ " you are invited to my dinner at 5pm")
print("Hello, " +guests[2]+ " you are invited to my dinner at 5pm")
print("Hello, " +guests[3]+ " you are invited to my dinner at 5pm")
print("Hello, " +guests[4]+ " you are invited to my dinner at 5pm")
print("Hello, " +guests[5]+ " you are invited to my dinner at 5pm")
print("NVM, Only two of yall can come lol")
uninvited=guests.pop()
print("Sorry that I changed my mind "+ uninvited)
uninvited=guests.pop()
print("Sorry that I changed my mind "+ uninvited)
uninvited=guests.pop()
print("Sorry that I changed my mind "+ uninvited)
uninvited=guests.pop()
print("Sorry that I changed my mind "+ uninvited)
print(guests[0]+ " You can still come lol")
print(guests[1]+ " You can still come lol")
del guests[1]
del guests[0]
print(guests)









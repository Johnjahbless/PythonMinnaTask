UserName = input("Enter your name" )
UserAge = int (input ("Enter your age" ))
ThisYear = 2018
BirthDay = ThisYear - int(UserAge)
Age50 = BirthDay + int(50)
print ("Hello %s you will be 50 years old by %d " %( UserName, Age50))
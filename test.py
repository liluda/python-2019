a = int(input("Enter the hour: "))
b = int(input("Enter the minute:"))

tb = ((a * 60) + b)
tb = (tb + 15)
ta = int(tb / 60)
nb = tb % 60
na = ta % 12
if na < 1: 
	na = 12
print ("Hours: " ,na)  
print ("Minutes: " ,nb)

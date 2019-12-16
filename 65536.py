import random
sentence = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string=""
for i in range(0,65536):
	string+=sentence[random.randint(0,25)]
print(string)

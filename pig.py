import random
pt = 0
ct = 0
cts = 0
prs = 0 
print("Welcome to pig")
print("")
start = str(input("type Roll to begin:"))
rollState = "Roll"
while(pt < 100 or ct < 100):
	while (rollState == "Roll" or  rollState == "r" or  rollState == "roll"):
		d6 = random.randint(1,6)
		if(d6 >= 2):
			print("You got a " + str(d6))
			prs += d6
			print("Your score for this round is " + str(prs))
			rollState = str(input("Keep or roll again: "))
		elif (d6 == 1):
			print("Looks like you got a " + str(d6))
			prs = 0
			rollState = str(input("Hit enter to countiue"))
		keep = int(prs + pt)
		print("Your total score is now " + str(keep))
		print("cpu plays here")
if (pt >= 100):
	print("You won wow")
elif (ct >= 100):
	print("You lost but that is reasonable it is a pretty hard bot")
else :
	print("broken code")

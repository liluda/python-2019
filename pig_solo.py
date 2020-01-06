import random
pt = 0
ct = 0
cts = 0
pts = 0
gamestatus = "true"
playerturn = 0

print("   Welcome to Pig   ")
print("--------------------")

while (gamestatus == "true"):
	while (pts <= 99 or cts <= 99):
		while (playerturn == 0):
			d6 = random.randint(1,6)
			x = str(input("roll "))
			if (d6 >= 2):
				if (x == "roll" or x == "r"):
					print(d6)
					pt += d6
					print("your running score is now " + str(pt))
				elif(x == "keep" or x == "k"):
					pts += pt
					print("your total score is now " + str(pts))
					pt = 0
					playerturn = 1
				else:
					print("ya broke it")
			elif(d6 == 1):
				pt = 0
				print(d6)
				print("your total score is now " + str(pts))
				playerturn = 1
		d6 = random.randint(1,6)
		cpu = random.randint(1,2)
		if (d6 >= 2):
			if (cpu == 1):
				print(d6)
				ct = (d6 + ct)
			elif(cpu == 2):
				ct += d6
				cts += ct
				print(d6)
				print("cpu score is now " + str(cts))
				ct = 0
				playerturn = 0
			else:
				print("it broke")
		elif(d6 == 1):
			ct = 0
			print(d6)
			print("cpu score is now " + str(cts))
			playerturn = 0
		gamestatus = "false"



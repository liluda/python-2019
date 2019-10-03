#basecon.py CMC
def bincon(num,addSpace):
	n = num
	s = addSpace
	print(n,s)
	d = 128
	binString = ""
	for i in range(0,8):
		q = int(n / d)
		r = int(n % d)
		print(d,q,r)
		n = r
		d = int(d / 2)
		binString = binString+str(q)
		if(s = 1 and i == 3):
			binString = binString = " "
	print(binString)

def main():
		bincon(191,0)
		bincon(7,0)
		bincon(15,0)
		bincon(31,0)
main()

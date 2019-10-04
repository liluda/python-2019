#basecon.py CMC CWC
def bincon(num,addSpace):
	n = num
	s = addSpace
	#print(n,s) #debug
	#print(n," = ",end="")
	d = 128
	binString ="" #create a string called binString
	for i in range(0,8):
		q = int(n / d)
		r = int(n % d)
		n = r
		d = int(d / 2)
		binString = binString+str(q)
		if(s == 1 and i == 3):
			binString = binString + " "
	#print(binString)
	return binString
	

# dechex.py CMC kenny
def hexcon(num):
	key = "0123456789abcdef" 
	h = ""
	h16 = int(num/16)
	h1 = num % 16
	h = key[h16]+ key[h1]
	return h
	

def main():
	bs = ""
	for i in range(0,256):
		bs = bincon(i,1)
		hs = ""
		hs = hexcon(i)
		print(i,bs,hs)
main()

#bincon_looop.py lil
#Convert a base 10 number to binary
#use 191 base 10 equal to 1011 1111 base 2
#q(quotient )#
n = int(input("# > 256: "))
n_orginal = n
d =128 
binstring = "" 
for i in range (0,8):
	q = int(n / d)
	r = int(n % d)
	print(d,q,r)
	n = r
	d = int(d / 2)
	binstring =binstring=str(q)
print("\n*********\t")
print()
print(str(n_orginal)+" base 10 = "+binstring+" base 2")
print("\n*********\t")



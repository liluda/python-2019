
def roots(a,b,c):
	D = (b*b - 4*a*c)
	print()
	print("D = " + str(D))
	if (D>= 0): 
		print("REAL ROOTS")
		D = D**.5 
		x1 = (-b + D) / (2*a)
		x2 = (-b - D) / (2*a)
		print("x1 = "+str(x1) +" x2 = "+str(x2))
		
	elif(D<0): 
		D = (D * -1)**.5
		print("IMAGINARY ROOTS")
		print("x1 = -"+str(b/(2*a))+" - "+str(D/(2*a))+"i")
		print("x2 = -"+str(b/(2*a))+" + "+str(D/(2*a))+"i")

if __name__ == '__main__':
	print("Input a,b and c for the quadratic (ax^2 + bx + c)")
	a = input("enter a: ")
	b = input("enter b: ")
	c = input("enter c: ")
roots(float(a), float(b), float(c))

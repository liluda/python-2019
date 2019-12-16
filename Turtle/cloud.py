import turtle
def main():
	obj= turtle.Turtle()
	scr= turtle.Screen()
	scr.setup(1920, 1080)
	obj.speed(0)
	cloud(obj)
	sun(obj)
	scr.exitonclick()



def cloud(obj):
	obj.color("black")
	count = 0
	obj.penup()
	obj.goto(800, 400)
	obj.pendown()
	while count < 2:
		count += 1 
		obj.fillcolor("grey")
		obj.begin_fill()
		obj.forward(150)
		obj.left(90)
		obj.forward(20)
		for x in range (1, 15):
			obj.left(10)
			obj.forward(10)
		obj.left(220)
		for y in range (1,18):
			obj.left(10)
			obj.forward(12)
		
		obj.left(200)
		for z in range (1,18):
			obj.left(10)
			obj.forward(15)
		obj.forward(18)
		obj.left(90)
		obj.forward(260)
		obj.penup()
		obj.goto(100, 300)
		obj.pendown()
		obj.end_fill()
	

	
		
def sun(obj):
	s = input("Is it a sunny day: ")
	s=s.lower()
	if (s.find('y') !=-1):
		obj.penup()
		obj.goto(-800, 400)
		obj.pendown()
		obj.forward(1)
		obj.fillcolor("orange")
		obj.begin_fill()
		obj.circle(500)
		obj.end_fill()



if __name__=="__main__":
	main()

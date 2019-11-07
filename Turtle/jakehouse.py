import turtle



def main(): # Make a square
	space = turtle.Screen() 
	space.setup(1920, 1080)         # create a turtle screen (space)
	bob = turtle.Turtle()            # create a turtle named bob
	house(bob,space)	
	space.exitonclick()		
def house(bob):
	bob.penup()
	bob.goto(-700, -75)
	bob.pendown()
	bob.begin_fill()
	bob.speed(0)
	bob.pensize(5)			#bob change pen thickness to 5
	bob.color ("moccasin")	
	bob.penup()
	bob.right(180)			
	bob.forward(200)		
	bob.right(180)
	bob.pendown()
	for count in range(4):
		bob.forward(400)          
		bob.right(90)             
	bob.end_fill()
	# Make a roof
	bob.begin_fill()
	bob.color ("red")
	bob.forward(450)          
	bob.right(-90)           
	bob.circle(250,180)           #
	bob.end_fill()
	#make a window

	bob.penup()				  
	bob.forward(150)		 
	bob.right(-90)			  
	bob.forward(100)
	bob.right(90)			
	bob.pendown()				
	bob.color ("blue")
	bob.begin_fill()
	bob.circle(50)	


	bob.end_fill()
	bob.left(90)
	bob.forward(100)
	bob.left(90)
	bob.penup()
	bob.forward(125)
	bob.pendown()

	#first mushroom white circle for roof
	bob.left(6)
	bob.penup()
	bob.forward(150)
	bob.right(90)
	bob.forward(175)
	bob.left(90)
	bob.color("white")
	bob.begin_fill()
	bob.pendown()
	bob.circle(50,365)
	bob.end_fill()

	#second mushroom circle on roof
	bob.penup()
	bob.left(90)
	bob.forward(300)
	bob.left(90)
	bob.forward(50)
	bob.pendown()
	bob.begin_fill()
	bob.circle(35)
	bob.end_fill()

	#window boards
	bob.penup()
	bob.forward(200)
	bob.right(97)
	bob.forward(10)
	bob.right(183)
	bob.color("brown")
	bob.pendown()
	bob.forward(100)
	bob.right(180)
	bob.forward(50)
	bob.right(90)
	bob.forward(57)
	bob.right(180)
	bob.forward(100)

	#door
	bob.penup()
	bob.left(90)
	bob.forward(200)
	bob.pendown()
	bob.color("brown")
	bob.begin_fill()
	bob.left(90)
	bob.circle(75,180)
	bob.forward(200)
	bob.left(89)
	bob.forward(150)
	bob.left(90)
	bob.forward(205)
	bob.left(90)
	bob.forward(150)
	bob.end_fill()
	bob.right(180)
					

if __name__ == '__main__':
	main()

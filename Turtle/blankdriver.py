import turtle
import cloud
import jakehouse 
import something
def main():
	w = turtle.Screen()
	w.setup(1920, 1080)
	#w.clear()
	w.bgcolor("#74CEF5")
	t = turtle.Turtle()
	jakehouse.house(t)
	cloud.cloud(t,w)
	something.driveSomething(t)
	w.exitonclick()
if __name__ == '__main__':
	main()

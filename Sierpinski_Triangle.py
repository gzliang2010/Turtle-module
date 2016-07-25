import turtle
from random import randint
from math import sqrt

#color = ["red", "blue", "yellow", "brown", "black", "green", "violet"]

def drawTriangle(point1, point2, point3, t):
	t.up()
	t.goto(point1[0], point1[1])
	t.down()
	t.goto(point2[0], point2[1])
	t.goto(point3[0], point3[1])
	t.goto(point1[0], point1[1])
	t.up()

def SierTriangle(point1, point2, point3, t):
	if (point1[0]-point2[0])**2+(point1[1]-point2[1])**2 > 15**2:
		
		point13 = [0.5*(point1[0]+point3[0]), 0.5*(point1[1]+point3[1])]
		point12 = [0.5*(point1[0]+point2[0]), 0.5*(point1[1]+point2[1])]
		point23 = [0.5*(point2[0]+point3[0]), 0.5*(point2[1]+point3[1])]

		# Draw the central triangle with random color fill
		t.fillcolor(randint(1,255), randint(1,255), randint(1,255))
		t.begin_fill()
		drawTriangle(point13, point23, point12, t)
		t.end_fill()

		SierTriangle(point1, point12, point13, t)
		SierTriangle(point12, point2, point23, t)
		SierTriangle(point13, point23, point3, t)

def main():
	myWin = turtle.Screen()
	t = turtle.Turtle()
	myWin.colormode(255) # Need this command, otherwise line24 and line 42 will cause error
	sideLen = 300.0
	point1 = [-sideLen/2, -sqrt(3)*sideLen/4]
	point2 = [sideLen/2, -sqrt(3)*sideLen/4]
	point3 = [0, sqrt(3)*sideLen/4]

	t.fillcolor(247, 238, 214)
	t.begin_fill()
	drawTriangle(point1, point2, point3, t)
	t.end_fill()
	SierTriangle(point1, point2, point3, t)
	t.hideturtle()
	myWin.exitonclick()
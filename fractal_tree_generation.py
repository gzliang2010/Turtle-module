import turtle
#from time import sleep
from random import randint

def tree(branchLen,t):
	if branchLen > 5:
		t.pensize(branchLen//10+1)
		t.forward(branchLen)
		#sleep(0.2)
		turnR = randint(15, 45)
		t.right(turnR)
		#sleep(0.2)
		tree(branchLen-randint(10,20), t)
		turnL = randint(15, 45)
		t.left(turnL+turnR)
		#sleep(0.2)
		tree(branchLen-randint(10,20), t)
		t.right(turnL)
		#sleep(0.2)
		t.backward(branchLen)
		#sleep(0.2)

def main():
	t = turtle.Turtle()
	myWin = turtle.Screen()
	t.left(90)
	t.up()
	t.backward(100)
	t.down()
	t.color("green")
	tree(100,t)
	myWin.exitonclick()
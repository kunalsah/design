import turtle
turtle.getscreen()
colors=['red','blue','purple','green','yellow','orange']
turtle.bgcolor("black")

for x in range(360):
	turtle.pencolor(colors[x%6])
	turtle.width(x/100+1)
	turtle.fd(x)
	turtle.lt(59)
turtle.done()
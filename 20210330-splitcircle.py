import turtle
turtle.pensize(2)
turtle.penup()
turtle.goto(0,150)
turtle.pendown()
turtle.circle(-150,)
for i in range (8):
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.seth(360/8*i) #想要n等分就360/n*i
    turtle.fd(150)
    turtle.goto(0,0)

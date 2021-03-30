import turtle
turtle.penup()
turtle.pensize(2)
turtle.goto(0,0)
for i in range(4):
    turtle.left(45)
    turtle.pendown()
    turtle.fd(150)
    turtle.left(90)
    turtle.circle(150,45)
    turtle.left(90)
    turtle.fd(150)
turtle.done()

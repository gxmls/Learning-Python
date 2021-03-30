import turtle
turtle.pensize(2)
for i in range(6):
    turtle.seth(60*i)
    turtle.fd(150)
    turtle.left(90)
    turtle.circle(150,30)
    turtle.goto(0,0)
turtle.done()

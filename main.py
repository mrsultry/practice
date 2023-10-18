import turtle

turtle.showturtle()
turtle.shape("turtle")
turtle.color("green")
turtle.shapesize(2)
distance = 100
steps = 6
angle = 360/steps
for i in range(steps):
    turtle.forward(distance)
    turtle.right(angle)
turtle.done()


import turtle

window = turtle.Screen()
draw = turtle.Turtle()
draw.color("orange")
draw.shape("turtle")
draw.pensize(2)
draw.speed(40)
#draw.left(90)
#draw.forward(100)

for i in range(1,37):    
    draw.forward(50)
    draw.right(60)
    draw.forward(50)
    draw.right(120)
    draw.forward(50)
    draw.right(60)
    draw.forward(50)
    draw.right(130)

draw.right(90)
draw.forward(150)
window.exitonclick()

import turtle
def draw_square(brad):
    for i in range(1,5):        
        brad.forward(100)
        brad.right(90)        

def draw_circle():    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    
    brad.color("orange")
    brad.circle(100)

def draw_triangle():
    brad = turtle.Turtle()
            
    brad.forward(100)
    brad.left(135)
    brad.forward(100)
    brad.left(90)
    brad.forward(100)
    brad.left(135)
    brad.forward(100)
            
window = turtle.Screen()
window.bgcolor("red")
brad = turtle.Turtle()
brad.shape("turtle")
brad.color("green")
brad.speed(20)
for i in range(1,37):
    draw_square(brad)
    brad.right(10)
#draw_circle()
#draw_triangle()
window.exitonclick()

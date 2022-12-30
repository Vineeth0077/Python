'''import turtle as t
import colorsys

t.bgcolor("black")
t.speed("fastest")
t.tracer(100)
t.pencolor("darkviolet")         #lights design
hue = 0.7
t.hideturtle()

def func():
    global hue
    for i in range(4):
        global hue
        for i in range(4):
            color = colorsys.hsv_to_rgb(hue, 1, 1)
            hue+=0.001
            t.fillcolor(color)
            t.begin_fill()
            t.fd(100)
            t.right(18)
            t.fd(100)
            t.lt(22)
            t.end_fill()

for j in range(400):
    func()
    t.goto(8, 8)
    t.rt(188)
    
t.exitonclick()'''

'''
t=turtle.Turtle() # corona virus design
s=turtle.Screen()
s.bgcolor("black")
t.pencolor("green")
a=0
b=0
t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()
while True:
    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    if b ==210:
        break
    t.hideturtle()

turtle.done()'''
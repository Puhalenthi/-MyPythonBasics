import turtle
t = turtle.Pen()
colors = ['blue', 'red', 'green', 'yellow']
t.speed(0)
turtle.bgcolor('black')
for i in range(0, 100):
    t.color(colors[i % 4])
    t.forward(i)
    t.left(90 + 1)
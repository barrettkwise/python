import turtle

rainbow = ["red", "tomato", "orangered", "coral", "darkorange", "orange", "gold", "yellow", "lawngreen", "greenyellow", "lime", "aquamarine", "cyan", "deepskyblue", "dodgerblue", "blue", "blueviolet", "violet", "fuchsia", "deeppink"]

shape = input("What shape of spiral would you like to draw? (square, circle, triangle) ").lower()
color = input("What color would you like your spiral to be? ")
thickness = int(input("How thick would you like your spiral to be? "))

if color in rainbow:
    pass
else:
    color = rainbow[0]

screen = turtle.Screen()
spiral = turtle.Turtle()
spiral.pensize(thickness)


if shape == "circle":
    for count, i in enumerate(rainbow):
        if count >= len(rainbow):
            spiral.pencolor(i)
        else:
            spiral.pencolor(i)

        spiral.forward(count / 4)
        spiral.right(15)

elif shape == "square":
    for i in range (0, 360, 1):
        if(color == "rainbow"):
            r = r + 1
            if(r >= len(rainbow)):
                r = 0
            spiral.pencolor(rainbow[r])
        else:
            spiral.pencolor(color)

        spiral.forward(i * 10)
        spiral.right(90)
elif(shape == "triangle"):
    for i in range (0, 360, 1):
        if(color == "rainbow"):
            r = r + 1
            if(r >= len(rainbow)):
                r = 0
            spiral.pencolor(rainbow[r])
        else:
            spiral.pencolor(color)

        spiral.forward(i * 20)
        spiral.left(120)


input()

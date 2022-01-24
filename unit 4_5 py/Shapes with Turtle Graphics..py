
from turtle import *
import sys

s = Screen()


def getcolorsandlw():
    lineColor = textinput("", "What line color would you like?")
    fillColor = textinput("", "What fill color would you like?")
    length = numinput("", "What length would you like?")
    width = numinput("", "What width would you like? (Enter 0 if drawing 3 or 4)")
    return lineColor, fillColor, length, width


def displayshape():
    print("1. Square")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Diamond")
    print("5. Parellelogram")
    print("6. Exit")
    choice = numinput("", "Please choose the number that goes with the shape you would like to see:")
    print(choice)
    return choice


def square(width, lineColor, fillColor):
    color(lineColor, fillColor)
    begin_fill()
    for i in range(4):
        forward(width)
        left(90)
    end_fill()


def rectangle(width, length, lineColor, fillColor):
    color(lineColor, fillColor)
    begin_fill()
    for i in range(2):
        forward(width)
        left(90)
        forward(length)
        left(90)
    end_fill()


def triangle(length, lineColor, fillColor):
    color(lineColor, fillColor)
    begin_fill()
    for i in range(1):
        forward(length)
        left(90)
        forward(length)
        left(60)
    end_fill()


def diamond(lineColor, fillColor, length):
    color(lineColor, fillColor)
    begin_fill()
    for i in range(2):
        forward(length)
        right(135)
        forward(length)
        right(45)
    end_fill()


def parellelogram(width, length, lineColor, fillColor):
    color(lineColor, fillColor)
    begin_fill()
    for i in range(2):
        forward(length * 3)
        right(135)
        forward(length * 3)
        right(45)
    end_fill()


def main():
    choice = displayshape()
    lineColor, fillColor, length, width = getcolorsandlw()
    if choice == 1:
        square(width, lineColor, fillColor)
    elif choice == 2:
        rectangle(width, length, lineColor, fillColor)
    elif choice == 3:
        triangle(length, lineColor, fillColor)
    elif choice == 4:
        diamond(lineColor, fillColor, length)
    elif choice == 5:
        parellelogram(width, length, lineColor, fillColor)
    elif choice == 6:
        sys.exit()


main()

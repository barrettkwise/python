import math
import sys

def displayoperation():
    print("1. Power")
    print("2. Factorial")
    print("3. Square Root")
    print("4. Degrees to Radians")
    print("5. Radians to Degrees")
    print("6. Exit")
    choice = str(input("Please choose the operation that you would like to preform:"))
    return choice
                 
def power():
    number1 = int(input("Please enter a positive whole number:"))
    number5 = int(input("Please select a number to raise your first number by:"))
    result = (number1)**(number5)
    print(result) 
    
def factorial():
    factorial = int(input("Please enter a positive whole number:"))
    result2 = math.factorial(factorial)
    print(result2)

def squareroot():
    number2 = int(input("Please enter a positive number:"))
    result3 = math.sqrt(number2)
    print(result3)
    
def degreestoradians():
    number3 = int(input("Please enter a number you want to covert to radians:"))
    radian = math.radians(number3)
    print(radian)

def radianstodegrees():
    number4 = int(input("Please enter a number you want to covert to degrees:"))
    degrees = math.degree(number4)
    print(degrees)

def exitprogram():
    sys.exit()

def choosingprogram(choice):
    if choice == "1":
        power()
    elif choice == "2":
        factorial()
    elif choice == "3":
        squareroot()
    elif choice == "4":
        degreestoradians()
    elif choice == "5":
        radianstodegrees()
    elif choice == "6":
        exitprogram()


def main():
    cont = "Y"
    while cont == "Y" or cont == "y":
        choice = displayoperation()
        choosingprogram(choice)
        cont = str(input("Do you want to continue? Press Y for yes or N for no."))


main()
    








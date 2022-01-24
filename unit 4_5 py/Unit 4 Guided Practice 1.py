def greeting():
    print("Welcome to my program!")

def numbers():
    ph = float(input("Enter the pH of your hot tub please:"))
    return ph

def logic(ph):
    if ph < 7.2:
        print("You need to add two teaspoons of pH increase.")
    elif ph >= 7.2 and ph <= 7.8:
here        print("The pH level is ok.")
    elif ph > 7.8:
        print("You need to add two teaspoons of pH decrease.")

def endofjob():
    print("Thank you for using my program!")

def main():
    keepgoing = "Y"
    while keepgoing == "y" or keepgoing == "Y":
        greeting()
        ph = numbers()
        logic(ph)
        keepgoing = input("Do you want to continue?")
        
    endofjob()

main()

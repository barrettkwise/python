def greeting():
    print("Welcome to the number adder thing!")

def goodbye():
    print("Thank you for using my number adder thing.")

def inpnumbers():
    usernumber = float(input("Please enter a number:"))
    return usernumber

def firstloop(usernumber):
    number = 0
    counter = 0
    while counter <= usernumber:
        number = number + counter
        counter = counter + 1
    return number

def main():

    keepgoing = "Y"
    while keepgoing == "y" or keepgoing == "Y":
        greeting()
        usernumber = inpnumbers()
        number = firstloop(usernumber)
        print (number)
        keepgoing = input("Do you wann to continue?")
        if keepgoing == "n" or keepgoing == "N":
            goodbye()

main()
    

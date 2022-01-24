def greeting():
    print("Welcome to our bank!")

def nameandbalance():
    name = input("What is your name?")
    balance = input("What is your balance?")
    return name,balance

def addressinfo():
    address = input("What is your house address?")
    return address

def printinfo(balance,address):
    print("Your balance is:" +balance)
    print("Your address is:" +address)

def endofjob():
    print("Thank you for visiting our bank!")

def main():

    greeting()
    keepgoing = "Y"
    while keepgoing == "y" or keepgoing == "Y":
        name,balance = nameandbalance()
        address = addressinfo()
        printinfo(balance,address)
        keepgoing = input("Do you want to continue?")


    endofjob()



main()

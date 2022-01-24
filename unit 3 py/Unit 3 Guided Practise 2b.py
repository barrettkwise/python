def welcome():
    name = str(input("What is your name?"))
    print(f"Welcome to my retirement calculator, {name}!")

def logic():
    age = int(input("What is your age?"))
    sentinelValue = 1

    while sentinelValue != -1:
        
        if age >= 65:
            print("You are of retirement age.")
        else:
            print("You are too young to retire.")

        print("Enter any number to continue, or -1 to exit.")
        sentinelValue = int(input("Please enter a number corresponding to the last nessage."))

def goodbye():
    print("Thank you for using my program!")


def main():
        welcome()
        logic()
        goodbye()
        
main()

def welcome():
    name = str(input("What is your name?"))
    print(f"Welcome to Pet Care, {name}!")
    

def info():
    sentinelval = 1
    while sentinelval != -1:
        name = str(input("What is your dog's name?"))
        breed = str(input("What is your dog's breed?"))
        age = int(input("What is your pet's age?"))
        weight = int(input("What is your pet's weight?"))
        print("Enter any number to continue, or -1 to exit.")
        sentinelval = int(input("Please enter a number corresponding to the last nessage."))
    return sentinelval,weight,name


def info2(sentinelval,weight,name):
     if sentinelval == -1:
        if weight >= 100 or weight <= 20:
            print(name) 
            
def goodbye():
    print("Thanks for coming to Pet Care!")


def main():
    welcome()
    sentinelval,weight,name = info()
    info2(sentinelval,weight,name)
    goodbye()

main()   
    


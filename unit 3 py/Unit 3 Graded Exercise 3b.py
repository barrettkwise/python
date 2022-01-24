def main():
    print("Welcome to our bank.")
    housekeeping()

def housekeeping():
    balance = float(input("Please enter your balance:"))
    numOverdrafts = float(input("How many times has the account been overdrawn?"))
    fee = (0.01 * balance) - (5 * numOverdrafts)
    print(f"The fee is {fee}")

    print("Thanks for visiting our bank and come again soon!")

main()

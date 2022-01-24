def main():
    
    l = float(input("Please enter your loan amount:"))
    y = float(input("Please enter your payment amount:"))
    m = 0
    x = 0
    
    while 1 >= 1:
        l = l - y
        m = m + 1
        print(f"Month {m} payment of {y} your loan balance of {l}")

        if l <= y:
            y = l
            m = m + 1
            l = 1 - 1
            l = l - l
            print(f"Month {m} payment of {y} your loan balance of {l}")

            if x == 0:
                con = float(input("Do you another loan to enter?(Yes = 1, No = 2)"))
                if con == 2:
                    print("To enter another loan, please restart the program.")
                if con == 1:
                    print("Thank your for using Bob’s E-Z Loan Calculator!")



main()

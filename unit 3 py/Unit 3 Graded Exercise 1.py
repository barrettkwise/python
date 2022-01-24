def greeting():
    print("Welcome to Jonas College tuition calculator!")

def endofjob():
    print("Thank you for using our tuition calculator!")

def tutcalculator():
    tuitioninc = 0.05
    tuition = 12000
    for year in range(5):
        tuitionfnl = tuition * tuitioninc
        tuitioninc = tuitioninc + 0.05
        year = year + 1
        
def main():
    greeting()
    tutcalculator()
    endofjob()


main()

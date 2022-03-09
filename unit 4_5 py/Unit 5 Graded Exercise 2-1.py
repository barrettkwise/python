def welcome():
    name = str(input("What is your name?"))
    print(f"Welcome to Skulling Financial Services, {name}!")
    return name

def logic1():
    year = 0
    yearsleft = int(input("How many years are left until you retire?"))
    annualam = int(input("How much can you save annually?"))
    saving = 0
    spending = 60000
    interest = 1.03
    yearsretired = 30 - yearsleft
    for year in range(yearsleft):
        saving = (saving + annualam) * interest
        saving = round(saving, 2)
        print(f"Year: {year} Savings: ${saving}")
    return year,yearsleft,annualam,saving,spending,interest,yearsretired

def logic2(year,yearsleft,annualam,saving,spending,interest,yearsretired):
    for year in range(yearsretired):
        saving = (saving - spending) * interest
        saving = round(saving, 2)
        print(f"Year: {yearsleft+year} Savings: ${saving}")
        if saving-spending <= 0:
        	print(f"You will run out of savings in year: {yearsl +year}")
        	break

def goodbye(name):
    print(f"Thanks for using Skulling Financial Services, {name}!")

def main():
    keepgoing = "Y"
    while keepgoing == "y" or keepgoing == "Y":
        name = welcome()
        year,yearsleft,annualam,saving,spending,interest,yearsretired = logic1()
        logic2(year,yearsleft,annualam,saving,spending,interest,yearsretired)
        keepgoing = input("Do you want to continue? Enter Y to continue.")

    goodbye(name)

main()
    
        
        
        
        
    

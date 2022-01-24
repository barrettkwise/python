num_list = [1,2,3,4,5]

def checkeven(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            return False

def main():
    checkeven(num_list)

main()

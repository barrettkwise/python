def valid_parentheses(string: str) -> bool:
    stack = []
    for s in string:
        if(s == '('):
            stack.append(s)
        elif(s == ')'):
            try:
                stack.pop()
            except:
                return False

    if(len(stack) == 0):
        return True
    else:
        return False

def main():
    user = str(input("Enter string: "))
    flag = valid_parentheses(user)
    print(flag)

main()



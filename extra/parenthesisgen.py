def balanced_parens(n: int) -> tuple[list, int]:
    ##eliminating non-changing cases
    if n == 0:
        return [""]
    elif n == 1:
        return ["()"]
    
    result = genpara(n)
    return result, len(result)
    
def genpara(n: int) -> list:
    result = []
    dfs(result, "", n, n)
    return result

def dfs(result: list, s: str, left: int, right: int) -> list:
    if left > right:
        return result
    if left == 0 and right == 0:
        result.append(s)
        return result
    
    if left > 0:
        dfs(result, s + "(", left - 1, right)
    
    if right > 0:
        dfs(result, s + ")", left, right - 1)

def main():
    print("Trying 10 or more sets can take very long. Do not try on weak computers, as it \nmay freeze computer.")
    user = int(input("Enter number of paranthesis sets: "))
    ans, length = balanced_parens(user)
    choice = str(input(f"Print result? May take extensive time to print all {length} solutions."))
    if choice.lower() == "y" or choice.lower() == "yes":
        print(f"All possible pairs: {ans}")

main()

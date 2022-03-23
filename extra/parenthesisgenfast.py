def balanced_parens(n: int) -> tuple[list, int]:
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans, len(ans)

def main():
    print("Trying 10 or more sets can take very long. Do not try on weak computers, as it \nmay freeze computer.")
    user = int(input("Enter number of paranthesis sets: "))
    ans, length = balanced_parens(user)
    choice = str(input(f"Print result? May take extensive time to print all {length} solutions."))
    if choice.lower() == "y" or choice.lower() == "yes":
        print(f"All possible pairs: {ans}")

main()
    

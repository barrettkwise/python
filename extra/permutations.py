import itertools as it

def permutations(string):
    perms = it.permutations(string)
    perms = list(perms)
    perms = ["".join(permutation) for permutation in perms]
    result = []
    [result.append(x) for x in perms if x not in result]
    print(f"{len(result)} possible permutations: {result}")
    return result

def main():
    string = str(input("Please input string: "))
    result = permutations(string)
    
main()

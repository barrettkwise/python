from sympy import *
from sympy.abc import x,y
import matplotlib.pyplot as plt
import math
from tabulate import tabulate 

def newtons_method(func, dfunc, x):

    def f(x):
        f = eval(func)
        return f
    
    def df(x):
        df = eval(dfunc)
        return df

    plt.xlabel("value of x")
    plt.ylabel("value of y")
    plt.title("Shift of x")
    vals = []
    while round(f(x), 3) != 0:
        vals.append([x, f(x)])
        i = x - (f(x)/df(x))
        x = i
    
    vals = add_dist(vals, (x, f(x)))
    print(tabulate(vals, numalign="center", tablefmt="orgtbl", headers=["X Values", "Y Values", f"Dist from {(round(x, 3), 0)}"]))
    plt.plot([i[0] for i in vals], [i[1] for i in vals], marker="o")
    plt.show()

def add_dist(cords, x):
    for cord in cords:
        dist = math.dist(cord, x)
        cord.append(dist)

    return cords
    

def main():
    func = input("Use proper syntax (2x = x*2) \nEnter function: ")
    dfunc = str(diff(func, x))
    s = float(input("Enter starting point: "))
    newtons_method(func, dfunc, s)

main()
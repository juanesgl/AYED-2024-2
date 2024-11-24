from sys import stdin 
import math 

def bisection(equation):
    low, high = 0, 1
    while low + 1e-9 < high:
        x = (low + high) / 2
        if equation(low) * equation(x) <= 0:
            high = x
        else:
            low = x
    return (low + high) / 2

def main():

    for line in stdin:
        p, q, r, s, t, u = map(float, stdin.readline().split())
        equation = lambda x: p * math.exp(-x) + q * math.sin(x) + r * math.cos(x) + s * math.tan(x) + t * x ** 2 + u
        if equation(0) * equation(1) > 0:
            print("No solution")
        else:
            print(f":.4f{bisection(equation)}")



    



    print(f"{equation(0):.4f}")
    print(f"No solution") 
main 
from sys import stdin
from math import factorial

def main():
    fact = [factorial(i) for i in range(10)]  
    line = stdin.readline().strip()

    while line:
        n = int(line)
        pos = 9
        res = 0
        
        while n > 0:
            if n >= fact[pos]:
                n -= fact[pos]
                res += 1
            else:
                pos -= 1
        
        print(res)
        line = stdin.readline().strip()

main()
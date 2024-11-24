from sys import stdin

def generate_factorials():
    fact = [1]
    for i in range(1, 10):
        fact.append(fact[-1] * i)
    return fact

def main():
    fact = generate_factorials()
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
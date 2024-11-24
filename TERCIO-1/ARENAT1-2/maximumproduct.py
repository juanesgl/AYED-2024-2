from sys import stdin

def main():

    data = stdin.read().split()
    positionition  = 0
    test_case = 0

    while position < len(data):
        N = int(data[position]) 
        position += 1  
        ans = 0  

        for i in range(position, position + N):
            prod = 1
            for j in range(i, position + N):
                prod *= int(data[j])
                if prod > ans:
                    ans = prod  

        test_case += 1  
        print(f"Case #{test_case}: The maximum product is {ans}.\n")  

        position += N  

main()
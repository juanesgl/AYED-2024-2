def main():
    testcase = int(input())
    
    while testcase > 0:
        testcase -= 1
        
        n, m = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        
        C = A + B
        C.append(0)
        
        A.sort()
        B.sort()
        C.sort()
        
        price = 0
        angry = float('inf')
        idx1, idx2 = 0, 0
        
        for i in range(n + m + 1):
            test = C[i]
            
            while idx1 < n and A[idx1] <= test:
                idx1 += 1
            
            while idx2 < m and B[idx2] < test:
                idx2 += 1
            
            v = n - idx1 + idx2
            
            if v < angry:
                angry = v
                price = test
        
        print(price, angry)

if __name__ == "__main__":
    main()


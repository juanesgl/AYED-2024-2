from sys import stdin

def main(): 
    B, N = list(map(int, stdin.readline().split()))  # B = #Banks N = #Transactions

    while B != 0 and N != 0:  #Close the cycle
        reserves = list(map(int, stdin.readline().split())) #Reserves [B1, B2, B3, ... ,BB]
        
        for _ in range(N):  #Transactions
            D, C, V = list(map(int, stdin.readline().split())) #D = Debtor bank
                                                               #C = Creditor bank
                                                               #V = Debenture bank
            reserves[D-1] -= V  #Debtor bank reserve, subtracts V
            reserves[C-1] += V  #Creditor bank reserve, add V 

        if all(r >= 0 for r in reserves): #If nothing negative exist
            print("S") 
        else:
            print("N")

        B, N = list(map(int, stdin.readline().split())) #More cases

main()
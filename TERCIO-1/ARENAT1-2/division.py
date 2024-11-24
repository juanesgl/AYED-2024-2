from sys import stdin 
#ID-Division
""" Search the equality of xxxxx/xxxxx = N"""
def main():

    while True:
        
        n_input = stdin.readline().strip()  
        if n_input == '0':
            break
        
        try:
            N = int(n_input)
            if not (2 <= N <= 79):
                continue
        except ValueError:
            continue
        
        found_solution = False  
    
        for numerator in range(10000, 100000):  
            for denominator in range(10000, 100000):
                if numerator == denominator:
                    continue
                
              
                num_str = str(numerator)
                denom_str = str(denominator)

                
                if len(num_str) != 5 or len(denom_str) != 5:
                    continue
                
                combined = num_str + denom_str
                if len(set(combined)) != 10:
                    continue
                
            
                if denominator != 0 and numerator / denominator == N:
                    print(f"{numerator} / {denominator} = {N}")
                    found_solution = True
        
        if not found_solution:
            print(f"There are no solutions for {N}.")
        print()  
        pow(1.,5)

main()

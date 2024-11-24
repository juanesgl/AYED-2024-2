from sys import stdin

def main():
    entry = stdin.read().strip().split('\n')
    
    for line in entry:
        H, U, D, F = map(float, line.split())
        if H == 0:
            return 
        
        height = 0
        day = 0
        fatigue = U * (F / 100)
        
        success = False
        failure = False
        
        while not success and not failure:
            day += 1
            height += U  
            
            if height > H:
                success = True
            else:
                U = max(0.0, U - fatigue)  
                height -= D  
                if height < 0:
                    failure = True
        
        if success:
            print(f"success on day {day}")
        else:
            print(f"failure on day {day}")

main()

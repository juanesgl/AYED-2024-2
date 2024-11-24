import sys
def main():
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    for line in data:
        H, U, D, F = map(float, line.split())
        if H == 0:
            break
        
        height = 0
        day = 0
        fatigue = U * (F / 100)
        
        while True:
            day += 1
            height += U
            if height > H:
                print(f"success on day {day}")
                break
            
            U = max(0.0, U - fatigue)
            height -= D
            
            if height < 0:
                print(f"failure on day {day}")
                break
main()

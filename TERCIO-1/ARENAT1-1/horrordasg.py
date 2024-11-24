import sys

def main():
    input = sys.stdin.read
    data = input().strip().split()
    
    number_of_cases = int(data[0])
    index = 1
    
    results = []
    
    for case_number in range(1, number_of_cases + 1):
        num_creatures = int(data[index])
        index += 1
        max_speed = -1
        
        for _ in range(num_creatures):
            creature_speed = int(data[index])
            index += 1
            
            if creature_speed > max_speed:
                max_speed = creature_speed
        
        results.append(f"Case {case_number}: {max_speed}")
    
    print("\n".join(results))

main()
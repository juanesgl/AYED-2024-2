import sys
import bisect

def generate_numbers(limit):
    numbers = set()
    i = 0
    while (2**i <= limit):
        j = 0
        while (2**i * 3**j <= limit):
            numbers.add(2**i * 3**j)
            j += 1
        i += 1
    return sorted(numbers)

def main():
    limit = 2**31  
    sorted_numbers = generate_numbers(limit)

    for line in sys.stdin:
        m = int(line.strip())
        if m == 0:
            break
        
        index = bisect.bisect_left(sorted_numbers, m)
        result = sorted_numbers[index]
        
        print(result)
        
main()

    
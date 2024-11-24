def calculate(name):
    total = 0
    for char in name:
        if 'a' <= char <= 'z':
            total += ord(char) - ord('a') + 1
        elif 'A' <= char <= 'Z':
            total += ord(char) - ord('A') + 1
    
    # Reduce to a single digit
    while total >= 10:
        temp = 0
        while total > 0:
            temp += total % 10
            total //= 10
        total = temp
    
    return total

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    i = 0
    while i < len(data) - 1:
        name1 = data[i].strip()
        name2 = data[i + 1].strip()
        
        first = calculate(name1)
        second = calculate(name2)
        
        if first < second:
            percentage = first * 100.0 / second
        else:
            percentage = second * 100.0 / first
        
        print(f"{percentage:.2f} %")
        
        i += 2

if __name__ == "__main__":
    main()

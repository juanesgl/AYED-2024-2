from sys import stdin
from collections import defaultdict

def read_input():
    cases = []
    lines = [line.strip() for line in stdin.read().splitlines()]
    i = 0
    
    while i < len(lines):
        if not lines[i]:
            i += 1
            continue
            
        parts = lines[i].split()
        
        if len(parts) == 2:
            N = int(parts[0])
            text = parts[1]
            cases.append((N, text))
        elif len(parts) == 1:
            N = int(parts[0])
            i += 1
            while i < len(lines) and not lines[i]:
                i += 1
            if i < len(lines):
                text = lines[i]
                cases.append((N, text))
        i += 1
    
    return cases

def find_password(N, text):
    freq = defaultdict(int)
    max_freq = 0
    current_pass = None
    
    for i in range(len(text) - N + 1):
        substr = text[i:i+N]
        freq[substr] += 1
        
        if (freq[substr] > max_freq or 
            (freq[substr] == max_freq and  (current_pass is None or substr < current_pass))):
            max_freq = freq[substr]
            current_pass = substr
    
    return current_pass

def main():
    cases = read_input()
    for N, text in cases:
        password = find_password(N, text)
        print(password)

if __name__ == "__main__":
    main()
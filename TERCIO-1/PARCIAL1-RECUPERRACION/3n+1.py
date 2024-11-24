from sys import stdin

collatz_lengths = {}

def collatz_conjecture(n):
    if n == 1:
        return 1

    if n in collatz_lengths:
        return collatz_lengths[n]
    
    if n % 2 == 0:
        next_n = n // 2
    else:
        next_n = 3 * n + 1
    
    collatz_lengths[n] = 1 + collatz_conjecture(next_n)
    return collatz_lengths[n]

def collatz_max_sequence(n, m):
    if n > m:
        n, m = m, n  
    
    max_sequence = 0
    for i in range(n, m + 1):
        sequence_length = collatz_conjecture(i)
        if sequence_length > max_sequence:
            max_sequence = sequence_length

    return max_sequence

def main():
    for line in stdin:
        numbers = line.split()
        n = int(numbers[0])
        m = int(numbers[1])
        result = collatz_max_sequence(n, m)
        print(f"{n} {m} {result}")

main()

from sys import stdin

# Memoization dictionary to store computed Collatz sequence lengths
memo = {}

def collatz_conjecture(n):
    # Base case: the Collatz sequence for 1 is 1 step
    if n == 1:
        return 1
    
    # If the sequence length for n is already computed, return it
    if n in memo:
        return memo[n]
    
    # Calculate next term based on even/odd rule
    if n % 2 == 0:
        next_n = n // 2
    else:
        next_n = 3 * n + 1
    
    # Compute the sequence length recursively and store it in memo
    memo[n] = 1 + collatz_conjecture(next_n)
    return memo[n]

def collatz_max_sequence(n, m):
    if n > m:
        n, m = m, n  # Swap to ensure n <= m
    
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
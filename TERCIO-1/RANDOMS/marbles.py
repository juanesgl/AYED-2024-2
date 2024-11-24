from sys import stdin

def binary_search(A, x):
    low, high = 0, len(A) - 1
    while low <= high:
        mid = (low + high) // 2
        if A[mid] == x:
            return mid
        elif A[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return low

def main():

    cases = 1
    N, Q = map(int, stdin.readline().strip().split())

    while N != 0 and Q != 0:
        marble_numbers = []

        
        for chees in range(N):
            marble_numbers.append(int(stdin.readline().strip()))

        
        marble_numbers.sort()

        print(f"CASE# {cases}:")
       
        for pizza in range(Q):
            list_of_marbles = int(stdin.readline().strip())
            position = binary_search(marble_numbers, list_of_marbles)

           
            if position < len(marble_numbers) and marble_numbers[position] == list_of_marbles:
                print(f"{list_of_marbles} found at {position + 1}")
                
            else:
                print(f"{list_of_marbles} not found")

        cases += 1
        N, Q = map(int, stdin.readline().strip().split())

main()

from sys import stdin

def binary_search(A, K):
    low, high = 0, len(A)
    while low < high:
        mid = (low + high) // 2
        if A[mid] < K:
            low = mid + 1
        else:
            high = mid
    return low

def main():
    case_number = 1
    while True:
        N, Q = map(int, stdin.readline().strip().split())
        
        if N == 0 and Q == 0:
            break

        numbers = []

        for salami in range(N):
            numbers.append(int(stdin.readline().strip()))

        numbers.sort()

        print(f"CASE# {case_number}:")

        for jalapeño in range(Q):

            query = int(stdin.readline().strip())
            binay_search_index = binary_search(numbers, query)
            
            if binay_search_index < len(numbers) and numbers[binay_search_index] == query:
                print(f"{query} found at {binay_search_index+ 1}")
            else:
                print(f"{query} not found")
        
        case_number += 1

main()
from sys import stdin

def binary_search(A, k):
    low, high = 0, len(A) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if A[mid] == k:
            result = mid
            high = mid - 1  
        elif A[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    return result

def main():
  
  N, Q = map(int, stdin.readline().split())
  case = 1

  while N != 0 and Q != 0:
    marbles = []
    queries = []

    marbles = [int(stdin.readline().strip()) for _ in range(N)]
    queries = [int(stdin.readline().strip()) for _ in range(Q)]

    marbles.sort()

    print(f"CASE# {case}:")
    for x in queries:
        found = binary_search(marbles, x)
        if found != -1:
          print(f"{x} found at {found + 1}")
        else:
          print(f"{x} not found")

    N, Q = map(int, stdin.readline().split())

    case += 1

main()
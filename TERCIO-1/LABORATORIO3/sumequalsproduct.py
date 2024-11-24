from sys import stdin
from bisect import bisect_left, bisect_right

def find_special_triplets(L, U):
    triplets = []

    # Precompute all possible triplets using two loops
    for a in range(100, int(U * 100) + 1):
        for b in range(a, int(U * 100) + 1):
            if a / 100 * b / 100 > 1:  # Ensure valid denominator
                c = (a / 100 + b / 100) / (a / 100 * b / 100 - 1)
                if b / 100 <= c <= U:  # Ensure c is in range and valid
                    sum_abc = a / 100 + b / 100 + c
                    triplets.append((sum_abc, a / 100, b / 100, c))

    # Sort the triplets by their sum
    triplets.sort()

    # Extract the sums for binary search
    sums = [triplet[0] for triplet in triplets]

    # Find and print valid triplets within the range [L, U]
    left = bisect_left(sums, L)
    right = bisect_right(sums, U)

    for i in range(left, right):
        sum_abc, a, b, c = triplets[i]
        print(f"{sum_abc:.2f} = {a:.2f} + {b:.2f} + {c:.2f} = {sum_abc:.2f}")

def main():
    line = stdin.readline().strip()
    L, U = map(float, line.split())
    find_special_triplets(L, U)

main()

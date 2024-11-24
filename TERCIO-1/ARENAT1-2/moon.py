
from sys import stdin as lilmoon
#Destroy the moon to save the earth

def binary_search(milims, secs):
    low, high = -1, milims + 1
    while low + 1 < abs(high):
        mid = low + ((abs(high) - low) // 2) # mid = low + ((abs(high) - low) >> 1)
        if mid * secs <= abs(milims):
            low = mid
        else:
            high = mid
    return low

def main():

    entry = int(lilmoon.readline())

    for wiggle in range(entry):
        T, S, D = map(int, input().split())
        seconds = T * 86400
        milim = D * 1000000
        estado = milim/seconds
        result = binary_search(milim, seconds)

        if estado > 1:
            print(f"Remove {result} tons")
        elif estado < 0:
            print(f"Add {result} tons")
        else:
            print("Add 0 tons")

main()
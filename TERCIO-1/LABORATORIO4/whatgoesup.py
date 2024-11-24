from sys import stdin
from bisect import bisect_left

def longest_increasing_subsequence(nums):
    if not nums:
        return 0, []

    tail = []
   
    parent = [-1] * len(nums)
   
    pos = [-1] * len(nums)
    
    lis_length = 0
    lis_end = 0
    
    for i, num in enumerate(nums):

        idx = bisect_left(tail, num)
        
        if idx < len(tail):
            tail[idx] = num
        else:
            tail.append(num)

        pos[idx] = i
        if idx > 0:
            parent[i] = pos[idx - 1]
        
        if idx + 1 > lis_length:
            lis_length = idx + 1
            lis_end = i

    lis = []
    while lis_end != -1:
        lis.append(nums[lis_end])
        lis_end = parent[lis_end]
    
    lis.reverse()
    
    return lis_length, lis

def main():
    nums = [int(line.strip()) for line in stdin]
    
    length, subsequence = longest_increasing_subsequence(nums)
    
    print(length)
    print("-")
    for num in subsequence:
        print(num)

main()
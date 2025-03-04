from sys import stdin

def verify_full(vessels, containers, max_capacity):
    containers_used = 1
    sum = 0

    for milk in vessels:
        if sum + milk > max_capacity:
            containers_used += 1
            sum = milk
            if containers_used > containers:
                return False
        else:
            sum += milk
    
    return True

def min_max_capacity(vessels, containers):
    left = max(vessels)
    right = sum(vessels)

    while left < right:
        mid = (left + right) >> 1
        if verify_full(vessels, containers, mid):
            right = mid
        else:
            left = mid + 1

    return left

def main():
    line = list(map(int, stdin.readline().split()))
    while len(line) != 0:
        containers = line[1]
        vessels = list(map(int, stdin.readline().split())) 
        res = min_max_capacity(vessels, containers)
        print(res)
        line = list(map(int, stdin.readline().split()))

main()
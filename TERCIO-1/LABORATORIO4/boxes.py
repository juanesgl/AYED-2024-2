from sys import stdin

def max_stacked_boxes(num_boxes, box_weights, box_loads):
    MAX_WEIGHT = 3000
    MAX_LOAD = 3000

    dp = [0] * (MAX_WEIGHT + MAX_LOAD + 1)
    
    for i in range(num_boxes - 1, -1, -1):
        weight = box_weights[i]
        load = box_loads[i]
        
        for available_load in range(load, -1, -1):
            if dp[available_load] > 0:
                dp[available_load + weight] = max(dp[available_load + weight], dp[available_load] + 1)
        
        if dp[weight] == 0:
            dp[weight] = 1
    
    return max(dp)

def main():
    input = stdin.read
    data = input().strip().split()
    
    idx = 0
    results = []
    
    while idx < len(data):
        num_boxes = int(data[idx])
        idx += 1
        if num_boxes == 0:
            break
        
        box_weights = []
        box_loads = []
        
        for _ in range(num_boxes):
            weight = int(data[idx])
            load = int(data[idx + 1])
            idx += 2
            box_weights.append(weight)
            box_loads.append(load)
        
        results.append(max_stacked_boxes(num_boxes, box_weights, box_loads))
    
    for result in results:
        print(result)
        
main()





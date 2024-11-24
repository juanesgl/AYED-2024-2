from sys import stdin
import heapq

def find_k_smallest_sums(k, arrays):
    base_sums = sorted(arrays[0])   
    for current_row in range(1, k):
        current_array = sorted(arrays[current_row])
        min_heap = []              
        for i in range(k):
            min_heap.append((base_sums[i] + current_array[0], 0))
        heapq.heapify(min_heap)            
        for i in range(k):
            current_sum, current_pos = heapq.heappop(min_heap)
            base_sums[i] = current_sum
            if current_pos + 1 < k:
                next_sum = current_sum - current_array[current_pos] + current_array[current_pos + 1]
                heapq.heappush(min_heap, (next_sum, current_pos + 1))   
    return base_sums
def main():
    for line in stdin:
        k = int(line)
        arrays = []       
        for _ in range(k):
            arrays.append([int(x) for x in input().split()])           
        result = find_k_smallest_sums(k, arrays)
        print(*result) #Envés de print(" ".join(map(str, result)))
main()
import heapq
from sys import stdin


def main():
    lines = stdin.read().strip().splitlines()
    pos = 0
    T = int(lines[pos])  
    pos += 1
    
    for _ in range(T):
        n, k = map(int, lines[pos].split())  
        pos += 1
        
        medication_queue = []
        
        for i in range(n):
            medicine_name, frequency = lines[pos].split() 
            frequency = int(frequency)
          
            heapq.heappush(medication_queue, (frequency, i, medicine_name, frequency))
            pos += 1
       
        for _ in range(k):
            current_time, idx, medicine_name, frequency = heapq.heappop(medication_queue)
            print(f"{current_time} {medicine_name}")
           
            heapq.heappush(medication_queue, (current_time + frequency, idx, medicine_name, frequency))

main()
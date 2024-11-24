from sys import stdin
import heapq

def main():
    
    TC = stdin.readline().strip()

    while TC != '':

        TC = int(TC)
        
        queue = []
        stack = []
        priority_queue = []
        
        is_queue = is_stack = is_priority_queue = True

        for _ in range(TC):
            x, y = map(int, stdin.readline().strip().split())

            if x == 1:
                
                queue.append(y)
                stack.append(y)
                heapq.heappush(priority_queue, -y)  

            elif x == 2:
                
                if not queue or not stack or not priority_queue:
                    is_queue = is_stack = is_priority_queue = False

                else:
                    if queue.pop(0) != y:
                        is_queue = False
                    if stack.pop() != y:
                        is_stack = False
                    if -heapq.heappop(priority_queue) != y:
                        is_priority_queue = False

        if is_queue and not is_stack and not is_priority_queue:
            print("queue")
        elif is_priority_queue and not is_queue and not is_stack:
            print("priority queue")
        elif is_stack and not is_queue and not is_priority_queue:
            print("stack")
        elif not is_queue and not is_stack and not is_priority_queue:
            print("impossible")
        else:
            print("not sure")

        TC = stdin.readline().strip()

main()

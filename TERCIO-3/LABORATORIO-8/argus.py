import heapq
from sys import stdin as funky

def func_entry():
    lines = funky.read().strip().splitlines()
    
    assert lines #Assert para asegurar que la lista no esté vacía
    
    queries = []
    for line in lines:
        if line == '#':
            break
        parts = line.split()
        
        assert len(parts) >= 3 #Assert para asegurar que la lista tenga al menos 3 elementos
        
        if parts[0] == 'Register':
            Qnum = int(parts[1])
            Period = int(parts[2])
            
            assert isinstance(Qnum, int) and Qnum > 0 and isinstance(Period, int) and Period > 0 #Assert para asegurar que Qnum y Period sean enteros positivos
           
            queries.append((Qnum, Period))

    K = 0
    if lines and lines[-1].isdigit():
        K = int(lines[-1])
        assert K >= 0
    
    return queries, K


def process_queries(queries, K):
   
    assert queries #Assert para asegurar que la lista no esté vacía
    assert K > 0 #Assert para asegurar que K sea mayor a 0
    
    heap = [(period, Qnum, period) for Qnum, period in queries]
    heapq.heapify(heap)
    
    result = []
    for _ in range(K):
        if not heap:
            break
        next_time, Qnum, period = heapq.heappop(heap)
        result.append(Qnum)
        
        assert isinstance(next_time, int) #Assert para asegurar que next_time sea un entero
        
        heapq.heappush(heap, (next_time + period, Qnum, period))
    
    assert len(result) == K #Assert para asegurar que la longitud de result sea igual a K
    
    return result


def main():
    queries, K = func_entry()
    
    if queries and K > 0:
        result = process_queries(queries, K)
        for qnum in result:
            print(qnum)

main()

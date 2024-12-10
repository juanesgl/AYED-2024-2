from sys import stdin

def is_bipartite(graph, node, colors, current_color) :
    
    colors[node] = current_color  
    for neighbor in graph[node]:
        if colors[neighbor] == -1:  
           
            if not is_bipartite(graph, neighbor, colors, 1 - current_color):
                return False
            
        elif colors[neighbor] == current_color:  
            return False
        
    return True

def main():
    
    num_nodes = int(stdin.readline().strip())
    
    while num_nodes != 0:
        
        num_edges = int(stdin.readline().strip())
        
        graph = [[] for _ in range(num_nodes)]
        for _ in range(num_edges):
            node1, node2 = map(int, stdin.readline().strip().split())
            
            graph[node1 - 1].append(node2 - 1)
            graph[node2 - 1].append(node1 - 1)
        
        colors = [-1] * num_nodes
    
        if is_bipartite(graph, 0, colors, 0):
            print("BICOLORABLE.")
            
        else:
            print("NOT BICOLORABLE.")
        
        num_nodes = int(stdin.readline().strip())

main()

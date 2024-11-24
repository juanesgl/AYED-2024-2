from sys import stdin

def dfs(graph: list, x: int, color: list, paint: int) -> int:
    color[x] = paint 
    for adj in graph[x]:
        if color[adj] == -1:  # Si el nodo no está coloreado
            if not dfs(graph, adj, color, 1-paint):
                return 0
        elif color[adj] == paint:  # Si el nodo adyacente tiene el mismo color
            return 0
    return 1 

def main():

    nodes = int(stdin.readline().strip())
    while nodes != 0:  # Primera condición de parada
        edges = int(stdin.readline().strip())
        
        # Construir el grafo
        graph = [[] for _ in range(nodes)]

        for i in range(edges):
            a, b = map(int, stdin.readline().strip().split())
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)
            
        # Verificar si es bicolorable
        color = [-1 for _ in range(nodes)]

        if dfs(graph, 0, color, 0):
            print("BICOLORABLE.")
        else:
            print("NOT BICOLORABLE.")
            
        # Leer el siguiente caso
        nodes = int(stdin.readline().strip())
        
main()

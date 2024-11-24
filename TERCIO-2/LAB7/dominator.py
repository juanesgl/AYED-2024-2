from sys import stdin 

def dfs(x: int, node: int, visited: list, adj_list: list):
    visited[x] = True
    if x == node:  # Si es el nodo que queremos eliminar, regresamos.
        return 
    for k in adj_list[x]:
        if not visited[k]:
            dfs(k, node, visited, adj_list)

def main():
    test_cases = int(stdin.readline().strip())
    counter = 1

    for _ in range(test_cases):
        nodes = int(stdin.readline().strip())
        graph = [[] for _ in range(nodes)]

        # Leer la matriz de adyacencia y crear la lista de adyacencia
        for i in range(nodes):
            row = [int(x) for x in stdin.readline().split()]
            for j in range(nodes):
                if row[j]:
                    graph[i].append(j)

        # Realizar DFS desde el nodo 0, sin eliminar ningún nodo
        visited = [False] * nodes
        dfs(0, -1, visited, graph)

        print(f'Case {counter}:')
        counter += 1

        for i in range(nodes):
            visited2 = [False] * nodes
            dfs(0, i, visited2, graph)  # Realizar DFS eliminando el nodo i

            print('+', '-' * (2 * nodes - 1), '+', sep='')
            print('|', end='')

            for j in range(nodes):
                # Si el nodo j es alcanzable desde 0 y se desconecta al eliminar i
                if visited[j] and (i == j or not visited2[j]):
                    print('Y|', end='')
                else:
                    print('N|', end='')

            print()

        print('+', '-' * (2 * nodes - 1), '+', sep='')

main()

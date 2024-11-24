from collections import defaultdict
from sys import stdin

def Toposort(graph: dict, nodes: list) -> list:
    topological_order = []
    visited = set()
    current_path = set()

    for node in sorted(nodes):
        if node not in visited:
            if not DFS_Toposort(graph, node, visited, current_path, topological_order):
                raise AssertionError("El grafo contiene ciclos y no se puede realizar un ordenamiento topológico.")

    return topological_order[::-1]

def DFS_Toposort(graph: dict, node: str, visited: set, current_path: set, topological_order: list) -> bool:
    visited.add(node)
    current_path.add(node)

    for neighbor in sorted(graph[node]):
        if neighbor not in visited:
            if not DFS_Toposort(graph, neighbor, visited, current_path, topological_order):
                return False
        elif neighbor in current_path:
            return False  

    current_path.remove(node)
    topological_order.append(node)
    return True

def find_all_orderings(graph: dict, nodes: list) -> None:
   
    visited = set()
    dependencies = {n: 0 for n in nodes} 

    for node in nodes:
        for neighbor in graph[node]:
            dependencies[neighbor] += 1

    generate_orderings(graph, nodes, visited, dependencies, [])

def generate_orderings(graph: dict, nodes: list, visited: set, dependencies: dict, path: list) -> None:

    if len(path) == len(nodes):
        print(''.join(path))
        return
    
    for node in filter(lambda n: n not in visited and dependencies[n] == 0, sorted(nodes)):
        visited.add(node)
        for neighbor in graph[node]:
            dependencies[neighbor] -= 1
        path.append(node)

        generate_orderings(graph, nodes, visited, dependencies, path)

        path.pop()
        visited.remove(node)
        for neighbor in graph[node]:
            dependencies[neighbor] += 1

def main():
    line_number = 0
    is_first_case = True

    for line in stdin:
        line = line.strip()
        if line_number % 2 == 0:
            nodes = line.split()  
        else:
            constraints = line.split() 
            graph = defaultdict(list)
            for j in range(0, len(constraints), 2):
                node_1, node_2 = constraints[j], constraints[j + 1]
                graph[node_1].append(node_2)

            if not is_first_case:
                print()
            is_first_case = False

            find_all_orderings(graph, nodes)

        line_number += 1
main()

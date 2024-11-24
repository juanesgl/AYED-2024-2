from collections import defaultdict
from sys import stdin

def Toposort(graph: dict, nodes: list) -> list:
    """
    Realiza un ordenamiento topológico en el grafo dirigido acíclico (DAG).
    Si el grafo contiene ciclos, lanza una AssertionError.
    """
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
            return False  # Se encontró un ciclo

    current_path.remove(node)
    topological_order.append(node)
    return True

def find_all_orderings(graph: dict, nodes: list) -> None:
    """
    Encuentra y muestra todas las ordenaciones topológicas posibles del grafo
    dadas las restricciones.
    """
    visited = set()
    dependencies = {n: 0 for n in nodes}  # Número de dependencias (aristas entrantes)

    # Calcular las dependencias de cada nodo
    for node in nodes:
        for neighbor in graph[node]:
            dependencies[neighbor] += 1

    # Genera todas las posibles ordenaciones usando la función recursiva
    generate_orderings(graph, nodes, visited, dependencies, [])

def generate_orderings(graph: dict, nodes: list, visited: set, dependencies: dict, path: list) -> None:
    """
    Genera todas las posibles ordenaciones topológicas mediante backtracking.
    """
    if len(path) == len(nodes):
        print(''.join(path))
        return

    # Filtramos los nodos que no han sido visitados y que no tienen dependencias pendientes
    for node in filter(lambda n: n not in visited and dependencies[n] == 0, sorted(nodes)):
        visited.add(node)
        for neighbor in graph[node]:
            dependencies[neighbor] -= 1
        path.append(node)

        generate_orderings(graph, nodes, visited, dependencies, path)

        # Deshacer los cambios al volver atrás (backtrack)
        path.pop()
        visited.remove(node)
        for neighbor in graph[node]:
            dependencies[neighbor] += 1

def main():
    index = 0
    is_first_case = True

    # Leer la entrada desde stdin
    for line in stdin:
        line = line.strip()
        if index % 2 == 0:
            nodes = line.split()  # Lista de nodos (a, b, c, ...)
        else:
            constraints = line.split()  # Lista de restricciones (pares de nodos)
            graph = defaultdict(list)
            for j in range(0, len(constraints), 2):
                node_1, node_2 = constraints[j], constraints[j + 1]
                graph[node_1].append(node_2)

            if not is_first_case:
                print()
            is_first_case = False

            find_all_orderings(graph, nodes)

        index += 1

if __name__ == "__main__":
    main()


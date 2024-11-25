import math
import heapq
from sys import stdin

def union(vertex1, vertex2, parent, rank):
    root1, root2 = find(vertex1, parent), find(vertex2, parent)

    if root1 == root2:
        return False 

    if rank[root1] == rank[root2]:
        parent[root2] = root1
        rank[root1] += 1
    elif rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
    return True 

def find(vertex, parent):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent[vertex], parent)
    return parent[vertex]

def compute_mst(n, edges):
    parent = list(range(n))
    rank = [1] * n
    mst_edges = []

    while edges:
        cost, vertex1, vertex2 = heapq.heappop(edges)
        if union(vertex1, vertex2, parent, rank):
            mst_edges.append(cost)
        if len(mst_edges) == n - 1:
            break

    return mst_edges

def compute_road_and_rail_distances(mst_edges, threshold):
    state_count = 1
    road_sum = 0
    rail_sum = 0

    for distance_squared in mst_edges:
        if distance_squared > threshold ** 2:
            state_count += 1
            rail_sum += math.sqrt(distance_squared)
        else:
            road_sum += math.sqrt(distance_squared)

    return state_count, road_sum, rail_sum

def main():
    input = stdin.read
    data = input().split()
    index = 0

    test_cases = int(data[index])
    index += 1

    results = []
    
    for case_number in range(test_cases):
        n = int(data[index])
        r = int(data[index + 1])
        index += 2

        points = []
        for _ in range(n):
            x, y = int(data[index]), int(data[index + 1])
            points.append((x, y))
            index += 2

        edge_list = []
        for i in range(n):
            for j in range(i + 1, n):
                dist_squared = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                heapq.heappush(edge_list, (dist_squared, i, j))

        mst_edges = compute_mst(n, edge_list)
        state_count, road_sum, rail_sum = compute_road_and_rail_distances(mst_edges, r)

        results.append(f"Case #{case_number + 1}: {state_count} {round(road_sum)} {round(rail_sum)}")

    for result in results:
        print(result)

main()

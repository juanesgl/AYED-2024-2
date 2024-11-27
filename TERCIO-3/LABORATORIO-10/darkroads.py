import sys
import heapq

def create(n, father, rank):
    father[n] = n
    rank[n] = 1

def findSet(n, father):
    if father[n] != n:
        father[n] = findSet(father[n], father)
    return father[n]

def union(i, j, father, rank):
    pi = findSet(i, father)
    pj = findSet(j, father)

    if pi != pj:
        if rank[pi] < rank[pj]:
            father[pi] = pj
        else:
            father[pj] = pi
            if rank[pi] == rank[pj]:
                rank[pi] += 1
        return True
    return False

def kruskal(graph, m, father, rank):
    cont = 0
    c = 0
    for edge in graph:
        if c == m - 1:
            break
        if union(edge[1], edge[2], father, rank):
            c += 1
            cont += edge[0]
    return cont

def main():
    input = sys.stdin.read
    data = input().split()
    index = 0

    while True:
        m = int(data[index])
        n = int(data[index + 1])
        index += 2
        if m == 0 and n == 0:
            break

        graph = []
        father = {}
        rank = {}
        total_cost = 0

        for i in range(m):
            create(i, father, rank)

        for i in range(n):
            x = int(data[index])
            y = int(data[index + 1])
            z = int(data[index + 2])
            graph.append([z, x, y])
            total_cost += z
            index += 3

        graph.sort(key=lambda edge: edge[0])
        mst_cost = kruskal(graph, m, father, rank)
        print(total_cost - mst_cost)

if __name__ == "__main__":
    main()

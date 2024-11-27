from sys import stdin, stdout
import heapq

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(n, edges):
    uf = UnionFind(n)
    mst_cost = 0
    edges.sort(key=lambda x: x[2])
    for u, v, cost in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_cost += cost
    return mst_cost

def main():
    input = stdin.read().strip().split('\n')
    index = 0
    results = []
    
    while index < len(input):
        if input[index].strip() == '':
            index += 1
            continue
        
        N = int(input[index].strip())
        index += 1
        
        T = []
        for _ in range(N - 1):
            u, v, cost = map(int, input[index].strip().split())
            T.append((u - 1, v - 1, cost))
            index += 1
        
        K = int(input[index].strip())
        index += 1
        
        new_lines = []
        for _ in range(K):
            u, v, cost = map(int, input[index].strip().split())
            new_lines.append((u - 1, v - 1, cost))
            index += 1
        
        M = int(input[index].strip())
        index += 1
        
        original_lines = []
        for _ in range(M):
            u, v, cost = map(int, input[index].strip().split())
            original_lines.append((u - 1, v - 1, cost))
            index += 1
        
        original_cost = kruskal(N, T)
        all_lines = original_lines + new_lines
        new_cost = kruskal(N, all_lines)
        
        results.append(f"{original_cost}\n{new_cost}")
    
    stdout.write("\n\n".join(results) + "\n")

if __name__ == "__main__":
    main()
from sys import stdin

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

def main():
    data = stdin.read().splitlines()  # Use stdin.read() for better input handling
    something = 0

    while something < len(data):
        n, m = map(int, data[something].strip().split())
        if n == 0 and m == 0:
            break
        
        father = list(range(n))
        rank = [0] * n
        
        for _ in range(m):
            something += 1
            group = list(map(int, data[something].strip().split()))
            k = group[0]
            members = group[1:]
            for i in range(1, k):
                union(members[0], members[i], father, rank)
        
        suspect_set = findSet(0, father)
        suspects = sum(1 for i in range(n) if findSet(i, father) == suspect_set)
        
        print(suspects)
        something += 1

if __name__ == "__main__":
    main()

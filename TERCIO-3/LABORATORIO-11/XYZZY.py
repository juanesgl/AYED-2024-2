from sys import stdin

def parse_input(n):

    energy = [None] * (n + 1)
    doors = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        room = list(map(int, stdin.readline().split()))
        energy[i] = room[0]
        doors[i] = list(filter(lambda x: x <= n, room[2:]))
        while len(doors[i]) != room[1]:
            doors[i].extend(list(filter(lambda x: x <= n, map(int, stdin.readline().split()))))
            
    return energy, doors

def bellman_ford(n, energy, doors):

    dist = [float('-inf')] * (n + 1)
    dist[1] = 100
    for _ in range(n - 1):
        for u in range(1, n + 1):
            if dist[u] <= 0: continue
            for v in doors[u]:
                dist[v] = max(dist[v], dist[u] + energy[v])
    return dist

def propagate_cycle(n, energy, doors, dist):

    for _ in range(n - 1):
        has_cycle = False
        for u in range(1, n + 1):
            if dist[u] <= 0: continue
            for v in doors[u]:
                if dist[u] + energy[v] > dist[v]:
                    has_cycle = True
                    dist[v] = float('inf')
        if not has_cycle: return

def main():

    n = int(stdin.readline())
    while n != -1:
        energy, doors = parse_input(n)
        dist = bellman_ford(n, energy, doors)
        propagate_cycle(n, energy, doors, dist)
        if dist[n] > 0:
            print('winnable')
        else:
            print('hopeless')
        n = int(stdin.readline().strip())

if __name__ == "__main__":
    main()

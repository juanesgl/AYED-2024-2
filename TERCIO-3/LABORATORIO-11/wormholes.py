from sys import stdin

def bellman_ford(star_systems, wormholes):
    dist = [float('inf')] * star_systems
    dist[0] = 0  

    
    for _ in range(star_systems):
        updated = False
        for x, y, t in wormholes:
            if dist[y] > dist[x] + t:
                dist[y] = dist[x] + t
                updated = True
        if not updated:
            break  

  
    for x, y, t in wormholes:
        if dist[y] > dist[x] + t:
            return True  

    return False  

def read_input():
    test_cases = int(stdin.readline())
    cases = []
    for _ in range(test_cases):
        star_systems, wormhole_count = map(int, stdin.readline().split())
        wormholes = [
            tuple(map(int, stdin.readline().split()))
            for _ in range(wormhole_count)
        ]
        cases.append((star_systems, wormholes))
    return cases

def process_cases(cases):
    results = []
    for star_systems, wormholes in cases:
        result = "possible" if bellman_ford(star_systems, wormholes) else "not possible"
        results.append(result)
    return results

def main():
    cases = read_input()  
    results = process_cases(cases) 
    print("\n".join(results))  

if __name__ == "__main__":
    main()

from sys import stdin

def find_root(enterprise, parent, cumulative_distance):
    if parent[enterprise] != enterprise:
        original_parent = parent[enterprise]
        root, distance_to_root = find_root(original_parent, parent, cumulative_distance)
        parent[enterprise] = root
        cumulative_distance[enterprise] += distance_to_root
    return parent[enterprise], cumulative_distance[enterprise]

def connect_enterprises(enterprise1, enterprise2, parent, rank, cumulative_distance):
    root1, distance1 = find_root(enterprise1, parent, cumulative_distance)
    root2, distance2 = find_root(enterprise2, parent, cumulative_distance)

    if root1 != root2:
        parent[root1] = root2
        cumulative_distance[root1] = distance2 + abs(enterprise1 - enterprise2) % 1000
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def process_test_case(data, current_position):
    position = current_position
    num_enterprises = int(data[position].strip())
    position += 1
    
    parent = list(range(num_enterprises + 1))
    rank = [0] * (num_enterprises + 1)
    cumulative_distance = [0] * (num_enterprises + 1)
    
    results = []
    
    while position < len(data) and data[position].strip() != "O":
        command = data[position].strip().split()
        position += 1
        
        if command[0] == 'E':
            enterprise = int(command[1])
            _, distance = find_root(enterprise, parent, cumulative_distance)
            results.append(str(distance))
        elif command[0] == 'I':
            enterprise1 = int(command[1])
            enterprise2 = int(command[2])
            connect_enterprises(enterprise1, enterprise2, parent, rank, cumulative_distance)
    
    return results, position + 1

def main():
    input_data = stdin.read().splitlines()
    current_position = 0
    num_test_cases = int(input_data[current_position].strip())
    current_position += 1
    
    results = []
    
    for _ in range(num_test_cases):
        test_case_results, current_position = process_test_case(input_data, current_position)
        results.extend(test_case_results)
    
    print(*results, sep="\n")

if __name__ == "__main__":
    main()

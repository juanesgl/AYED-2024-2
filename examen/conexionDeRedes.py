from sys import stdin

def find_set(node, parent):
    
    while node != parent[node]:
        parent[node] = parent[parent[node]]
        node = parent[node]
    return node

def union_sets(node1, node2, parent, rank):
 
    root1 = find_set(node1, parent)
    root2 = find_set(node2, parent)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1

def process_single_test_case(input_lines, start_line):
    current_line = start_line
    if input_lines[current_line].strip() == " ":
        current_line += 1

    total_computers = int(input_lines[current_line].strip())
    current_line += 1

    parent = [i for i in range(total_computers + 1)]
    rank = [0] * (total_computers + 1)

    successful_queries = 0
    unsuccessful_queries = 0

    while current_line < len(input_lines) and input_lines[current_line].strip():
        command = input_lines[current_line].strip().split()
        current_line += 1

        if command[0] == 'c':  
            computer1, computer2 = int(command[1]), int(command[2])
            union_sets(computer1, computer2, parent, rank)
            
        elif command[0] == 'q':  
            computer1, computer2 = int(command[1]), int(command[2])
            if find_set(computer1, parent) == find_set(computer2, parent):
                successful_queries += 1
            else:
                unsuccessful_queries += 1

    return successful_queries, unsuccessful_queries, current_line

def main():

    input_lines = stdin.read().splitlines()
    current_line = 0
    test_cases = int(input_lines[current_line].strip())
    current_line += 1

    results = []

    for _ in range(test_cases):
        successful, unsuccessful, current_line = process_single_test_case(input_lines, current_line)
        results.append(f"{successful},{unsuccessful}")


    print("\n\n".join(results))

if __name__ == "__main__":
    main()
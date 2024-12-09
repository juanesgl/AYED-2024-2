from sys import stdin

def findSet(n, parent):
    if parent[n] != n:
        parent[n] = findSet(parent[n], parent)
    return parent[n]

def union(i, j, parent, rank):
    root_i = findSet(i, parent)
    root_j = findSet(j, parent)

    if root_i != root_j:
        if rank[root_i] < rank[root_j]:
            parent[root_i] = root_j
        else:
            parent[root_j] = root_i
            if rank[root_i] == rank[root_j]:
                rank[root_i] += 1

def process_test_case(data, start_index):
    index = start_index
    if data[index].strip() == "":
        index += 1
    
    num_computers = int(data[index].strip())
    index += 1
    
    parent = list(range(num_computers + 1))
    rank = [0] * (num_computers + 1)
    
    successful_queries = 0
    unsuccessful_queries = 0
    
    while index < len(data) and data[index].strip() != "":
        command = data[index].strip().split()
        index += 1
        
        if command[0] == 'c':
            computer_i = int(command[1])
            computer_j = int(command[2])
            union(computer_i, computer_j, parent, rank)
        elif command[0] == 'q':
            computer_i = int(command[1])
            computer_j = int(command[2])
            if findSet(computer_i, parent) == findSet(computer_j, parent):
                successful_queries += 1
            else:
                unsuccessful_queries += 1
    
    return successful_queries, unsuccessful_queries, index

def main():
    input_data = stdin.read().splitlines()
    current_line = 0
    num_test_cases = int(input_data[current_line].strip())
    current_line += 1
    
    results = []
    
    for _ in range(num_test_cases):
        successful, unsuccessful, current_line = process_test_case(input_data, current_line)
        results.append(f"{successful},{unsuccessful}")
    
    print("\n\n".join(results))

if __name__ == "__main__":
    main()